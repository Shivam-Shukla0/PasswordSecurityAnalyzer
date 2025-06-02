import streamlit as st
import pandas as pd
import io
from datetime import datetime
from password_analyzer import PasswordAnalyzer
from security_tips import SecurityTips

def main():
    st.set_page_config(
        page_title="Password Security Analyzer",
        page_icon="🔐",
        layout="wide"
    )
    
    st.title("🔐 Password Security Analyzer")
    st.markdown("**Cybersecurity tool for analyzing password strength and security practices**")
    
    # Initialize analyzer
    analyzer = PasswordAnalyzer()
    security_tips = SecurityTips()
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Choose a section:",
        ["Password Analyzer", "Security Education", "Batch Analysis", "Security Report"]
    )
    
    if page == "Password Analyzer":
        password_analyzer_page(analyzer)
    elif page == "Security Education":
        security_education_page(security_tips)
    elif page == "Batch Analysis":
        batch_analysis_page(analyzer)
    elif page == "Security Report":
        security_report_page(analyzer)

def password_analyzer_page(analyzer):
    st.header("Real-time Password Analysis")
    
    # Password input
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Enter Password to Analyze")
        password = st.text_input(
            "Password:",
            type="password",
            help="Your password is processed locally and never sent to any server",
            key="main_password"
        )
        
        show_password = st.checkbox("Show password", key="show_main")
        if show_password and password:
            st.text(f"Password: {password}")
    
    with col2:
        st.subheader("Security Notice")
        st.info("🔒 All analysis is performed locally. Your password never leaves your device.")
    
    if password:
        # Analyze password
        analysis = analyzer.analyze_password(password)
        
        # Display strength score
        st.subheader("Password Strength Score")
        score = analysis['score']
        
        # Color-coded progress bar
        if score >= 80:
            color = "green"
            strength_text = "Strong"
        elif score >= 60:
            color = "orange"
            strength_text = "Medium"
        else:
            color = "red"
            strength_text = "Weak"
        
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.progress(score / 100)
        with col2:
            st.metric("Score", f"{score}/100")
        with col3:
            st.markdown(f"**{strength_text}**")
        
        # Detailed analysis
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Security Metrics")
            
            # Basic metrics
            st.write(f"**Length:** {analysis['length']} characters")
            st.write(f"**Entropy:** {analysis['entropy']:.2f} bits")
            st.write(f"**Character Variety:** {analysis['character_variety']}/4 types")
            
            # Character types
            st.write("**Character Types Used:**")
            for char_type, present in analysis['character_types'].items():
                icon = "✅" if present else "❌"
                st.write(f"{icon} {char_type.replace('_', ' ').title()}")
        
        with col2:
            st.subheader("Security Issues")
            
            if analysis['issues']:
                for issue in analysis['issues']:
                    st.error(f"⚠️ {issue}")
            else:
                st.success("✅ No major security issues detected!")
            
            # Common password check
            if analysis['is_common']:
                st.error("🚨 This password appears in common password lists!")
            else:
                st.success("✅ Not found in common password databases")
        
        # Recommendations
        st.subheader("Security Recommendations")
        if analysis['recommendations']:
            for i, rec in enumerate(analysis['recommendations'], 1):
                st.write(f"{i}. {rec}")
        else:
            st.success("🎉 Excellent! Your password meets all security criteria.")
        
        # Pattern analysis
        if analysis['patterns']:
            with st.expander("🔍 Pattern Analysis (Advanced)"):
                st.write("**Detected patterns that may weaken security:**")
                for pattern in analysis['patterns']:
                    st.write(f"• {pattern}")

def security_education_page(security_tips):
    st.header("Password Security Education")
    
    tab1, tab2, tab3, tab4 = st.tabs(["Best Practices", "Common Mistakes", "Attack Methods", "Tools & Tips"])
    
    with tab1:
        st.subheader("Password Security Best Practices")
        tips = security_tips.get_best_practices()
        for tip in tips:
            st.write(f"• {tip}")
    
    with tab2:
        st.subheader("Common Password Mistakes")
        mistakes = security_tips.get_common_mistakes()
        for mistake in mistakes:
            st.error(f"❌ {mistake}")
    
    with tab3:
        st.subheader("Understanding Password Attacks")
        attacks = security_tips.get_attack_methods()
        for attack_name, description in attacks.items():
            with st.expander(f"🎯 {attack_name}"):
                st.write(description)
    
    with tab4:
        st.subheader("Password Management Tools & Tips")
        tools = security_tips.get_tools_and_tips()
        for category, items in tools.items():
            st.write(f"**{category}:**")
            for item in items:
                st.write(f"• {item}")
            st.write("")

def batch_analysis_page(analyzer):
    st.header("Batch Password Analysis")
    st.write("Analyze multiple passwords at once for organizational security assessments.")
    
    # Text area for multiple passwords
    passwords_text = st.text_area(
        "Enter passwords (one per line):",
        height=200,
        help="Each password should be on a separate line"
    )
    
    if st.button("Analyze All Passwords"):
        if passwords_text:
            passwords = [p.strip() for p in passwords_text.split('\n') if p.strip()]
            
            if passwords:
                results = []
                progress_bar = st.progress(0)
                
                for i, password in enumerate(passwords):
                    analysis = analyzer.analyze_password(password)
                    results.append({
                        'Password': password[:3] + '*' * (len(password) - 3),  # Mask password
                        'Score': analysis['score'],
                        'Strength': 'Strong' if analysis['score'] >= 80 else 'Medium' if analysis['score'] >= 60 else 'Weak',
                        'Length': analysis['length'],
                        'Entropy': round(analysis['entropy'], 2),
                        'Character Types': analysis['character_variety'],
                        'Common Password': 'Yes' if analysis['is_common'] else 'No',
                        'Issues Count': len(analysis['issues'])
                    })
                    progress_bar.progress((i + 1) / len(passwords))
                
                # Display results
                df = pd.DataFrame(results)
                st.subheader("Analysis Results")
                st.dataframe(df, use_container_width=True)
                
                # Summary statistics
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Total Passwords", len(results))
                with col2:
                    strong_count = len([r for r in results if r['Strength'] == 'Strong'])
                    st.metric("Strong Passwords", strong_count)
                with col3:
                    weak_count = len([r for r in results if r['Strength'] == 'Weak'])
                    st.metric("Weak Passwords", weak_count)
                with col4:
                    common_count = len([r for r in results if r['Common Password'] == 'Yes'])
                    st.metric("Common Passwords", common_count)
                
                # Download results
                csv = df.to_csv(index=False)
                st.download_button(
                    label="Download Results as CSV",
                    data=csv,
                    file_name=f"password_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv"
                )

def security_report_page(analyzer):
    st.header("Security Assessment Report")
    st.write("Generate a comprehensive security report based on password analysis.")
    
    # Test password for report generation
    test_password = st.text_input(
        "Enter a password to generate sample report:",
        type="password",
        help="This will generate a detailed security report"
    )
    
    if test_password and st.button("Generate Security Report"):
        analysis = analyzer.analyze_password(test_password)
        
        # Generate report content
        report_content = generate_security_report(analysis, test_password)
        
        # Display report
        st.subheader("Security Assessment Report")
        st.markdown(report_content)
        
        # Download report
        st.download_button(
            label="Download Report as Text",
            data=report_content,
            file_name=f"security_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain"
        )

def generate_security_report(analysis, password):
    """Generate a detailed security report"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    report = f"""
CYBERSECURITY PASSWORD ASSESSMENT REPORT
========================================

Report Generated: {timestamp}
Assessment Tool: Password Security Analyzer v1.0

EXECUTIVE SUMMARY
-----------------
Password Length: {analysis['length']} characters
Security Score: {analysis['score']}/100
Risk Level: {'LOW' if analysis['score'] >= 80 else 'MEDIUM' if analysis['score'] >= 60 else 'HIGH'}
Entropy: {analysis['entropy']:.2f} bits

DETAILED ANALYSIS
-----------------

Character Composition:
• Lowercase letters: {'Yes' if analysis['character_types']['lowercase'] else 'No'}
• Uppercase letters: {'Yes' if analysis['character_types']['uppercase'] else 'No'}
• Numbers: {'Yes' if analysis['character_types']['numbers'] else 'No'}
• Special characters: {'Yes' if analysis['character_types']['special_chars'] else 'No'}

Security Issues Identified:
"""
    
    if analysis['issues']:
        for issue in analysis['issues']:
            report += f"• {issue}\n"
    else:
        report += "• No significant security issues detected\n"
    
    report += f"""
Common Password Database Check:
• Status: {'FOUND - Password appears in common password lists' if analysis['is_common'] else 'NOT FOUND - Password not in common databases'}

RECOMMENDATIONS
---------------
"""
    
    if analysis['recommendations']:
        for i, rec in enumerate(analysis['recommendations'], 1):
            report += f"{i}. {rec}\n"
    else:
        report += "No specific recommendations - password meets security standards.\n"
    
    report += """
SECURITY BEST PRACTICES
-----------------------
1. Use unique passwords for each account
2. Enable two-factor authentication where available
3. Use a reputable password manager
4. Regularly update passwords for sensitive accounts
5. Never share passwords or store them in plain text

CONCLUSION
----------
This assessment provides a snapshot of password security based on current best practices.
Regular security assessments and adherence to best practices are recommended for maintaining optimal security posture.

---
Report generated by Password Security Analyzer
For questions or support, consult your IT security team.
    """
    
    return report

if __name__ == "__main__":
    main()
