import markdown
import google.generativeai as genai
from django.shortcuts import redirect


GOOGLE_API_KEY = 'AIzaSyAX8YiDkmNyeLhCnGZOZ4Uq_2gJyXvatNs'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# List of commands
commands = ["home", "Cart", "Shop", "Checkout", "Profile", "Payment", "Sign In", "Sign Up", "Forgot Password", 
            "Reset Password", "SignOut", "check_user_exists", "update_profile", "search", "verify_otp", 
             "submit_otp", "product", "add_to_cart", "remove_from_cart", "change_quantity", "order_confirmation", 
             "paycheck", "upload_audio", "trigger"]


def Call(speech):

    # Prompt for Gemini API
    prompt_for_gemini_api = f"Please provide the command from this list {commands} corresponding to the following speech: {speech}. The response should be in the format specified by the keys in the commands list"
    
    # Generate response using Gemini API
    response = model.generate_content(prompt_for_gemini_api)
    # parsed_response = markdown.markdown(response.text)
    value = response.text
    return value








