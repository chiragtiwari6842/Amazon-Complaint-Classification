import requests

def generate_reply(complaint, labels, website_under_maintainence = False):
    api_key = 'ADD YOUR API KEY and I'll HIDE MINE'
    gemini_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"
    headers = {
        "Content-Type": "application/json"
    }
    reply_dict = {
        'Positive Review': [
            "We're so glad to hear you liked the product. Please recommend us to your close ones too.",
            "Thank you for your kind words! We're thrilled to know you loved the product. Please feel free to share your experience with others."
        ],
        'Other': [
            "Sorry we couldn't quite understand your issue. Could you please provide more details or clarify what you'd like help with? We're here to assist you!",
            "We apologize, we weren't able to fully understand your issue. Can you please clarify what you're experiencing so we can better assist you?"
        ],
        'Website Bugs': [
            "We're sorry for the inconvenience, the website is currently under maintenance. Please try again after a while.",
            "Our website is currently down for maintenance. We apologize for the trouble, and we appreciate your patience during this time."
        ],
        'Account Access Issues': [
            "We're sorry for the inconvenience, the website is currently under maintenance. Please try again after a while.",
            "There may be a temporary issue with account access. Please try again after some time, and let us know if the problem persists."
        ],
        'Order Cancellations': [
            "You can surely cancel the product from the website. Just open 'My Orders' on the website and click the 'Cancel' button.",
            "To cancel your order, simply log in to the website, go to 'My Orders,' and select the 'Cancel' option."
        ],
        'Shipping Damages': [
            "Sorry to hear your product was damaged. We can offer a refund or an exchange, within 10 days of purchase.",
            "We sincerely apologize for the damaged product. You’re eligible for a refund or exchange within 10 days of purchase."
        ],
        'Wrong Item Received': [
            "Very sorry to hear you received the wrong item. Don't worry, we can offer a refund or an exchange, within 10 days of purchase.",
            "We apologize for sending the wrong item. We’re happy to assist you with a refund or exchange within 10 days of your purchase."
        ],
        'Product Not as Described': [
            "It's okay, you can still exchange or return with a 100% refund until 10 days of purchase.",
            "We understand your concern. You can exchange or return the product within 10 days of purchase for a full refund."
        ],
        'Product Quality': [
            "It's okay, you can still exchange or return with a 100% refund until 10 days of purchase.",
            "We’re sorry the product didn’t meet your expectations. You can exchange or return it within 10 days for a full refund."
        ],
        'Missing Items': [
            "We can return and re-order the purchase. We’re very sorry for your inconvenience.",
            "Apologies for the missing items. We will return and re-order the product to make sure you get everything you need."
        ],
        'Refund Request': [
            "Sure, we can guide you to get that refund. Please open the website, log in, go to 'Orders', select your order, and click 'Return Product'.",
            "To initiate the refund, please log into our website, go to your orders, and click the 'Return Product' option."
        ],
        'Payment Issues': [
            "If your payment was declined, please re-check all the details and try again. If you were charged twice, please immediately contact customer support team at some-random-number.",
            "We recommend reviewing your payment details and trying again. If you encounter double charges, please contact customer support right away."
        ],
        'Delivery Delay': [
            "We’re sorry for the delay in your delivery. Your order should arrive in a few days. Thanks for your patience!",
            "We apologize for the delay. Your order will be delivered in a few days. For your security."
        ],
        'Customer Service': [
            "We'll get back to you as soon as possible. We apologize for the delay and appreciate your patience.",
            "We apologize for the wait. Our customer service team is working on your request and will get back to you as soon as possible."
        ],
        'If sensitive info like tracking ID mentioned': [
            'Please refrain from adding sensitive information ',
            'Please dont give sensitive info here, thanks'
        ]
    }
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f'''Please generate a response to give back to the user and only give me the response
                        Complaint: "{complaint}"
                        Labels: "{labels}"
                        Responses Context: {reply_dict}
                        Website Under Maintaince: {website_under_maintainence == True}
                        Feel free to use your own words but try to generate a smaller response taking all the labels into consideration. 
                        And remember, this is the customer care response, so try to solve the error the best you could. But we still
                        can't access user's accounts. We're here to help only. and try humane resposnes instead of just apologizing for every tweet
                        and never ask anything back from the user. This is a one-on-one deal, gets done with your response.
                        If personal details mentioned, add a small sentence in the end to refrain from doing so. If it's multi label, don't just 
                        pick sentences from each of them, try to generate a single sentence. If personal info was necessary
                        for that complaint, don't inlcude the sensitive message. And no giving of contact numbers, this is the final
                        interaction with the user. And don't leave anything for supervision, your reply is directly going on twitter, hence don't 
                        make the reply longer than 15 words.'''
                    }
                ]
            }
        ]
    }

    response = requests.post(gemini_url, headers=headers, json=data)

    if response.status_code == 200:
        lst = response.json()
        result = lst['candidates'][0]['content']['parts'][0]['text']
        return result
    
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return "Error", []
