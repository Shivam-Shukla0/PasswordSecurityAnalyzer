"""
Security education content and tips for password security
"""

class SecurityTips:
    def __init__(self):
        pass
    
    def get_best_practices(self):
        """Return list of password security best practices"""
        return [
            "Use passwords that are at least 12 characters long",
            "Include a mix of uppercase letters, lowercase letters, numbers, and special characters",
            "Avoid using personal information like names, birthdays, or addresses",
            "Use unique passwords for each account - never reuse passwords",
            "Consider using passphrases made of random words instead of complex character combinations",
            "Enable two-factor authentication (2FA) whenever possible",
            "Use a reputable password manager to generate and store strong passwords",
            "Regularly update passwords for sensitive accounts (every 90 days for critical systems)",
            "Never share passwords via email, text, or other insecure methods",
            "Log out of accounts when finished, especially on shared computers",
            "Be cautious of phishing attempts asking for password information",
            "Use security questions with answers that aren't easily guessed or researched",
            "Monitor your accounts regularly for suspicious activity",
            "Keep your devices and browsers updated with security patches",
            "Use secure networks - avoid entering passwords on public Wi-Fi"
        ]
    
    def get_common_mistakes(self):
        """Return list of common password mistakes to avoid"""
        return [
            "Using the same password for multiple accounts",
            "Using personal information like pet names, birthdays, or family names",
            "Creating passwords that are too short (less than 8 characters)",
            "Using only letters or only numbers without variety",
            "Storing passwords in plain text files or sticky notes",
            "Using predictable patterns like '123456' or 'qwerty'",
            "Making passwords that are only slight variations of old ones",
            "Sharing passwords with friends, family, or colleagues",
            "Using default passwords on devices and accounts",
            "Writing passwords down in easily accessible places",
            "Using common words from the dictionary without modification",
            "Creating passwords based on current events or popular culture",
            "Using keyboard patterns like 'asdfgh' or '1qaz2wsx'",
            "Ignoring security warnings about compromised passwords",
            "Not updating passwords after security breaches"
        ]
    
    def get_attack_methods(self):
        """Return information about common password attack methods"""
        return {
            "Brute Force Attack": 
                "Attackers systematically try every possible combination of characters until they find the correct password. "
                "Longer, more complex passwords exponentially increase the time required for this attack to succeed. "
                "Defense: Use long passwords (12+ characters) with high entropy.",
            
            "Dictionary Attack": 
                "Attackers use lists of common passwords and dictionary words to guess passwords. "
                "This is why using common words or phrases makes passwords vulnerable. "
                "Defense: Avoid dictionary words and common passwords.",
            
            "Credential Stuffing": 
                "Attackers use previously breached username/password combinations to access other accounts. "
                "This exploits password reuse across multiple services. "
                "Defense: Use unique passwords for every account.",
            
            "Phishing": 
                "Attackers trick users into entering their passwords on fake websites or forms. "
                "These sites look legitimate but capture credentials for malicious use. "
                "Defense: Verify website URLs and use bookmarks for important sites.",
            
            "Social Engineering": 
                "Attackers manipulate people into revealing passwords through psychological manipulation, "
                "often by impersonating trusted individuals or creating urgent scenarios. "
                "Defense: Never share passwords and verify identity before providing information.",
            
            "Rainbow Table Attack": 
                "Attackers use precomputed tables of hash values to quickly crack password hashes. "
                "This is effective against common passwords and unsalted hashes. "
                "Defense: Use complex, unique passwords that wouldn't appear in rainbow tables.",
            
            "Keylogger Attack": 
                "Malicious software records keystrokes to capture passwords as they're typed. "
                "This can happen through infected software or compromised devices. "
                "Defense: Keep systems updated, use antivirus software, and consider 2FA.",
            
            "Shoulder Surfing": 
                "Attackers observe users typing passwords in public spaces or through security cameras. "
                "This is a physical security threat that doesn't require technical skills. "
                "Defense: Be aware of surroundings when entering passwords and shield input."
        }
    
    def get_tools_and_tips(self):
        """Return information about password management tools and tips"""
        return {
            "Password Managers": [
                "Use reputable password managers like Bitwarden, 1Password, or LastPass",
                "Enable automatic password generation for new accounts",
                "Use the password manager's browser extension for convenience",
                "Secure your password manager with a strong master password",
                "Enable two-factor authentication on your password manager account",
                "Regularly backup your password database",
                "Consider using a password manager with dark web monitoring"
            ],
            
            "Two-Factor Authentication (2FA)": [
                "Use authenticator apps like Google Authenticator or Authy",
                "Prefer app-based 2FA over SMS when possible",
                "Enable 2FA on all critical accounts (email, banking, social media)",
                "Keep backup codes in a secure location",
                "Consider hardware security keys for high-security needs",
                "Don't disable 2FA unless absolutely necessary"
            ],
            
            "Password Creation Techniques": [
                "Use the 'passphrase' method: combine random words with symbols",
                "Try the 'sentence method': take first letters of a memorable sentence",
                "Use the 'substitution method': replace letters with numbers/symbols",
                "Consider the 'diceware' method for truly random passphrases",
                "Make passwords memorable through stories or mental images",
                "Use acronyms from favorite quotes or song lyrics"
            ],
            
            "Account Security": [
                "Enable account lockout after failed login attempts",
                "Monitor login notifications and account activity",
                "Use security questions with non-obvious answers",
                "Regularly review and revoke unnecessary app permissions",
                "Keep contact information updated for account recovery",
                "Be cautious with 'remember me' options on shared devices"
            ],
            
            "Browser Security": [
                "Use browsers with built-in password managers carefully",
                "Enable automatic updates for security patches",
                "Be cautious with browser extensions that access passwords",
                "Clear saved passwords when using public computers",
                "Use private/incognito mode for sensitive activities",
                "Verify SSL certificates before entering passwords"
            ]
        }
    
    def get_entropy_explanation(self):
        """Explain password entropy concept"""
        return {
            "definition": "Password entropy measures the randomness and unpredictability of a password in bits.",
            "calculation": "Entropy = log₂(character_set_size^password_length)",
            "recommendations": {
                "Minimum entropy": "40 bits for basic security",
                "Good entropy": "60+ bits for strong security", 
                "Excellent entropy": "80+ bits for maximum security"
            },
            "factors": [
                "Character set size (alphabet, numbers, symbols)",
                "Password length",
                "Randomness (avoiding patterns and predictable sequences)",
                "Uniqueness (not found in common password lists)"
            ]
        }
    
    def get_compliance_guidelines(self):
        """Return compliance and organizational guidelines"""
        return {
            "NIST Guidelines": [
                "Minimum 8 characters for user passwords",
                "Minimum 12 characters for administrative passwords",
                "No periodic password changes unless compromise is suspected",
                "Screen passwords against common password lists",
                "Allow all printable ASCII characters including spaces",
                "No password hints or knowledge-based authentication"
            ],
            
            "ISO 27001": [
                "Implement formal password policy",
                "Regular security awareness training",
                "Monitor and log authentication attempts",
                "Implement account lockout mechanisms",
                "Use multi-factor authentication for sensitive systems"
            ],
            
            "Organizational Best Practices": [
                "Conduct regular password audits",
                "Provide password manager licenses to employees",
                "Implement privileged access management (PAM)",
                "Create incident response procedures for password breaches",
                "Regular security training and phishing simulations",
                "Establish clear password sharing prohibitions"
            ]
        }
