import re
import math
import string
from typing import Dict, List, Tuple
from common_passwords import COMMON_PASSWORDS

class PasswordAnalyzer:
    def __init__(self):
        self.common_passwords = set(COMMON_PASSWORDS)
        
    def analyze_password(self, password: str) -> Dict:
        """Comprehensive password analysis"""
        if not password:
            return self._empty_analysis()
        
        analysis = {
            'score': 0,
            'length': len(password),
            'entropy': self._calculate_entropy(password),
            'character_types': self._analyze_character_types(password),
            'character_variety': 0,
            'is_common': self._is_common_password(password),
            'patterns': self._detect_patterns(password),
            'issues': [],
            'recommendations': []
        }
        
        # Calculate character variety
        analysis['character_variety'] = sum(analysis['character_types'].values())
        
        # Calculate overall score
        analysis['score'] = self._calculate_score(password, analysis)
        
        # Generate issues and recommendations
        analysis['issues'] = self._identify_issues(password, analysis)
        analysis['recommendations'] = self._generate_recommendations(password, analysis)
        
        return analysis
    
    def _empty_analysis(self) -> Dict:
        """Return empty analysis for empty password"""
        return {
            'score': 0,
            'length': 0,
            'entropy': 0,
            'character_types': {
                'lowercase': False,
                'uppercase': False,
                'numbers': False,
                'special_chars': False
            },
            'character_variety': 0,
            'is_common': False,
            'patterns': [],
            'issues': ['Password is empty'],
            'recommendations': ['Enter a password to begin analysis']
        }
    
    def _calculate_entropy(self, password: str) -> float:
        """Calculate password entropy in bits"""
        if not password:
            return 0
        
        # Determine character set size
        charset_size = 0
        if re.search(r'[a-z]', password):
            charset_size += 26
        if re.search(r'[A-Z]', password):
            charset_size += 26
        if re.search(r'[0-9]', password):
            charset_size += 10
        if re.search(r'[^a-zA-Z0-9]', password):
            charset_size += 32  # Approximate special characters
        
        if charset_size == 0:
            return 0
        
        # Entropy = log2(charset_size^length)
        entropy = len(password) * math.log2(charset_size)
        
        # Reduce entropy for detected patterns
        pattern_penalty = len(self._detect_patterns(password)) * 5
        return max(0, entropy - pattern_penalty)
    
    def _analyze_character_types(self, password: str) -> Dict[str, bool]:
        """Analyze what types of characters are present"""
        return {
            'lowercase': bool(re.search(r'[a-z]', password)),
            'uppercase': bool(re.search(r'[A-Z]', password)),
            'numbers': bool(re.search(r'[0-9]', password)),
            'special_chars': bool(re.search(r'[^a-zA-Z0-9]', password))
        }
    
    def _is_common_password(self, password: str) -> bool:
        """Check if password is in common password lists"""
        return password.lower() in self.common_passwords
    
    def _detect_patterns(self, password: str) -> List[str]:
        """Detect common patterns that weaken passwords"""
        patterns = []
        
        # Sequential characters
        if re.search(r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)', password.lower()):
            patterns.append("Contains sequential alphabetic characters")
        
        if re.search(r'(123|234|345|456|567|678|789|890)', password):
            patterns.append("Contains sequential numeric characters")
        
        # Repeated characters
        if re.search(r'(.)\1{2,}', password):
            patterns.append("Contains 3+ repeated characters")
        
        # Keyboard patterns
        keyboard_patterns = ['qwert', 'asdf', 'zxcv', '12345', 'qazws']
        for pattern in keyboard_patterns:
            if pattern in password.lower():
                patterns.append(f"Contains keyboard pattern: {pattern}")
        
        # Common substitutions
        if re.search(r'[4@]', password) and 'a' not in password.lower():
            patterns.append("Uses common character substitution (4/@/a)")
        
        if re.search(r'[3]', password) and 'e' not in password.lower():
            patterns.append("Uses common character substitution (3/e)")
        
        if re.search(r'[1!]', password) and 'i' not in password.lower():
            patterns.append("Uses common character substitution (1/!/i)")
        
        # Date patterns
        if re.search(r'(19|20)\d{2}', password):
            patterns.append("Contains year pattern")
        
        if re.search(r'(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])', password):
            patterns.append("Contains date pattern")
        
        # Common words with numbers
        if re.search(r'(password|admin|user|login|welcome|secret)\d*', password.lower()):
            patterns.append("Contains common word with numbers")
        
        return patterns
    
    def _calculate_score(self, password: str, analysis: Dict) -> int:
        """Calculate overall password strength score (0-100)"""
        score = 0
        
        # Length scoring (0-25 points)
        length = len(password)
        if length >= 12:
            score += 25
        elif length >= 8:
            score += 15
        elif length >= 6:
            score += 10
        elif length >= 4:
            score += 5
        
        # Character variety (0-20 points)
        score += analysis['character_variety'] * 5
        
        # Entropy scoring (0-30 points)
        entropy = analysis['entropy']
        if entropy >= 60:
            score += 30
        elif entropy >= 40:
            score += 20
        elif entropy >= 20:
            score += 10
        elif entropy >= 10:
            score += 5
        
        # Pattern penalties (0-15 points deduction)
        pattern_penalty = len(analysis['patterns']) * 3
        score -= min(pattern_penalty, 15)
        
        # Common password penalty (-20 points)
        if analysis['is_common']:
            score -= 20
        
        # Bonus for very long passwords with high variety
        if length >= 16 and analysis['character_variety'] >= 3:
            score += 10
        
        # Bonus for high entropy passwords
        if entropy >= 80:
            score += 15
        
        return max(0, min(100, score))
    
    def _identify_issues(self, password: str, analysis: Dict) -> List[str]:
        """Identify specific security issues"""
        issues = []
        
        if len(password) < 8:
            issues.append("Password is too short (minimum 8 characters recommended)")
        
        if analysis['character_variety'] < 3:
            issues.append("Password lacks character variety (use uppercase, lowercase, numbers, and symbols)")
        
        if not analysis['character_types']['uppercase']:
            issues.append("Missing uppercase letters")
        
        if not analysis['character_types']['numbers']:
            issues.append("Missing numbers")
        
        if not analysis['character_types']['special_chars']:
            issues.append("Missing special characters")
        
        if analysis['entropy'] < 30:
            issues.append("Low password entropy (predictable)")
        
        if len(analysis['patterns']) > 2:
            issues.append("Multiple predictable patterns detected")
        
        if analysis['is_common']:
            issues.append("Password found in common password databases")
        
        # Check for personal information patterns
        if re.search(r'(admin|user|password|login|welcome|secret|123)', password.lower()):
            issues.append("Contains common dictionary words")
        
        return issues
    
    def _generate_recommendations(self, password: str, analysis: Dict) -> List[str]:
        """Generate specific recommendations for improvement"""
        recommendations = []
        
        if len(password) < 12:
            recommendations.append("Increase password length to at least 12 characters")
        
        if not analysis['character_types']['uppercase']:
            recommendations.append("Add uppercase letters (A-Z)")
        
        if not analysis['character_types']['lowercase']:
            recommendations.append("Add lowercase letters (a-z)")
        
        if not analysis['character_types']['numbers']:
            recommendations.append("Add numbers (0-9)")
        
        if not analysis['character_types']['special_chars']:
            recommendations.append("Add special characters (!@#$%^&*)")
        
        if analysis['patterns']:
            recommendations.append("Avoid predictable patterns and sequences")
        
        if analysis['is_common']:
            recommendations.append("Use a unique password not found in common lists")
        
        if analysis['entropy'] < 50:
            recommendations.append("Increase randomness by avoiding predictable combinations")
        
        # Advanced recommendations
        if analysis['score'] < 80:
            recommendations.extend([
                "Consider using a passphrase with random words",
                "Use a password manager to generate and store strong passwords",
                "Enable two-factor authentication for additional security"
            ])
        
        return recommendations
