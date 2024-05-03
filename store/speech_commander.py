import markdown
import google.generativeai as genai


GOOGLE_API_KEY = 'AIzaSyAX8YiDkmNyeLhCnGZOZ4Uq_2gJyXvatNs'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# List of commands
commands = [
    "home", "main page", "start",
    "cart", "view cart",
    "shop", "go shopping",
    "checkout", "proceed to checkout",
    "profile", "user profile",
    "payment", "make payment",
    "sign in", "login",
    "sign up", "register",
    "forgot password", "reset password",
    "logout", "sign out",
    "search", "search for products",
    "verify OTP", "submit OTP",
    "product details", "view product",
    "add to cart", "add item to cart",
    "remove from cart", "delete item from cart",
    "change quantity", "update quantity",
    "order confirmation", "confirm order",
    "payment status", "check payment status",
    "upload audio", "record audio",
    "trigger", "invoke action",
    # URLs with arguments
    "product 1", "view product 1",
    "product 2", "view product 2",
    "product 3", "view product 3",
    # Add more commands for other product IDs if needed
]



def Call(speech):

    # Prompt for Gemini API
    prompt_for_gemini_api = f"Please provide the command from this list {commands} corresponding to the following speech: {speech}"
    
    # Generate response using Gemini API
    response = model.generate_content(prompt_for_gemini_api)
    # response = model.generate_content(prompt)
    # print(markdown.markdown(response.text))
    parsed_response = markdown.markdown(response.text)
    return parsed_response




print(Call("Go to the shop page"))







