"""
Common passwords database for security analysis
This includes the most commonly used passwords from various security breaches and studies
"""

COMMON_PASSWORDS = [
    # Top 50 most common passwords
    "123456",
    "password",
    "123456789",
    "12345678",
    "12345",
    "1234567",
    "1234567890",
    "qwerty",
    "abc123",
    "111111",
    "123123",
    "admin",
    "letmein",
    "welcome",
    "monkey",
    "dragon",
    "pass",
    "master",
    "hello",
    "freedom",
    "whatever",
    "qazwsx",
    "trustno1",
    "654321",
    "jordan23",
    "harley",
    "password123",
    "iloveyou",
    "1234",
    "000000",
    "superman",
    "naruto",
    "123321",
    "666666",
    "password1",
    "sunshine",
    "princess",
    "football",
    "baseball",
    "soccer",
    "basketball",
    "charlie",
    "hunter",
    "shadow",
    "secret",
    "michael",
    "jordan",
    "daniel",
    "andrew",
    "joshua",
    
    # Keyboard patterns
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm",
    "1qaz2wsx",
    "qwerty123",
    "asdf1234",
    
    # Sequential patterns
    "abcdef",
    "fedcba",
    "abcd1234",
    "1234abcd",
    
    # Common variations
    "password!",
    "password@",
    "Password1",
    "Password123",
    "admin123",
    "root123",
    "user123",
    "guest123",
    "test123",
    "demo123",
    
    # Years and dates
    "2023",
    "2022",
    "2021",
    "2020",
    "1234567",
    "0123456789",
    
    # Names and words
    "jennifer",
    "melissa",
    "robert",
    "william",
    "christopher",
    "anthony",
    "jessica",
    "matthew",
    "ashley",
    "amanda",
    "nicole",
    "stephanie",
    "michelle",
    "elizabeth",
    "kimberly",
    "lisa",
    "angela",
    "heather",
    "brenda",
    "emma",
    "olivia",
    "sophia",
    "ava",
    "isabella",
    "mia",
    "charlotte",
    "abigail",
    "emily",
    "harper",
    "amelia",
    
    # Technology related
    "computer",
    "internet",
    "windows",
    "microsoft",
    "google",
    "facebook",
    "twitter",
    "instagram",
    "youtube",
    "amazon",
    "apple",
    "android",
    "iphone",
    "samsung",
    
    # Simple patterns
    "aaaaaa",
    "111111",
    "222222",
    "333333",
    "444444",
    "555555",
    "666666",
    "777777",
    "888888",
    "999999",
    "000000",
    
    # Common phrases
    "iloveyou",
    "ihateyou",
    "fuckyou",
    "loveme",
    "lovely",
    "family",
    "friends",
    "mother",
    "father",
    "sister",
    "brother",
    
    # Animals
    "cat",
    "dog",
    "bird",
    "fish",
    "horse",
    "tiger",
    "lion",
    "elephant",
    "monkey",
    "rabbit",
    
    # Colors
    "red",
    "blue",
    "green",
    "yellow",
    "black",
    "white",
    "orange",
    "purple",
    "pink",
    "brown",
    
    # Simple combinations
    "123abc",
    "abc123",
    "pass123",
    "123pass",
    "admin1",
    "root1",
    "user1",
    "guest1",
    "test1",
    "demo1"
]

# Convert to lowercase for case-insensitive comparison
COMMON_PASSWORDS = [pwd.lower() for pwd in COMMON_PASSWORDS]

# Add some uppercase and mixed case variations for common ones
ADDITIONAL_VARIATIONS = []
for pwd in COMMON_PASSWORDS[:20]:  # Only for top 20 to avoid huge list
    ADDITIONAL_VARIATIONS.extend([
        pwd.upper(),
        pwd.capitalize(),
        pwd + "1",
        pwd + "!",
        pwd + "123",
        "1" + pwd,
        "!" + pwd
    ])

COMMON_PASSWORDS.extend(ADDITIONAL_VARIATIONS)

# Remove duplicates and sort
COMMON_PASSWORDS = sorted(list(set(COMMON_PASSWORDS)))
