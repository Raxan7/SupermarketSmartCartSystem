import markdown
import re
import google.generativeai as genai


GOOGLE_API_KEY = 'AIzaSyAX8YiDkmNyeLhCnGZOZ4Uq_2gJyXvatNs'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

url_paths = ["home", "Cart", "Shop", "Checkout", "Profile", "Payment", "Sign In", "Sign Up", "Forgot Password", 
            "Reset Password", "SignOut", "check_user_exists", "update_profile", "search", "verify_otp", 
             "submit_otp", "product", "add_to_cart", "remove_from_cart", "change_quantity", "order_confirmation", 
             "paycheck", "upload_audio", "trigger"]


def separate_product(input_str):
    match = re.match(r"([a-zA-Z_ ]+)([0-9]+)", input_str)
    if match:
        return match.groups()
    else:
        return None

def Call(speech: str):
    # Prompt for Gemini API
    prompt_for_gemini_api = f"Please provide only one the command from this list {list(url_paths)} corresponding to the following speech: {speech}. The response should be in the format specified by the keys in the commands list, if you there is a number in words form, change it into numeric and append it to the command, don't return as a string"
    
    # Generate response using Gemini API
    response = model.generate_content(prompt_for_gemini_api)
    value = response.text
    print(value)

    # input_str = "product21"
    result = separate_product(value)
    print(result)
    try:
        if result:
            product_path, number = result
            print("Product:", product_path)
            print("Number:", number)
            return product_path, number
        elif (result==None):
            return value
        
    except TypeError as e:
        print(e)
        return value
    

def introText(page_name):
    prompt_for_gemini_api = f"Provide for me a short but brief welcome message for the {page_name} in my Ecommerce website"
    # Generate response using Gemini API
    response = model.generate_content(prompt_for_gemini_api)
    # parsed_response = markdown.markdown(response.text)
    value = response.text
    return value


# Example usage
# speech = "I want to purchase product twenty one"
# print(Call(speech))
# speech = "Nataka kununua bidhaa ya kwanza"
# print(Call(speech))
# speech = "Go to home page"
# print(Call(speech))
# speech = "Buy the first product"
# print(Call(speech))
# speech = "I want to add product thirty three to cart"
# print(Call(speech))
# speech = "Go to cart page"
# print(Call(speech))



