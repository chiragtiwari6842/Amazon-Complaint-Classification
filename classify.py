import joblib

def classify_into_categories(complaint):

    loaded_model = joblib.load("GBC_Classifier.pkl")

    categories = [
        "Delivery Delay", "Payment Issue", "Product Quality", "Order Cancellation", "Account Access Issue",
        "Customer Service", "Refund Request", "Shipping Damage", "Missing Items", "Wrong Item Received",
        "Product Not as Described", "Positive Review", "Website Bugs", "Order Tracking Problem", "Other",
        "Payment Issues", "Delivery Issues", "Product Issues", "Account Issues", "Customer Support Issues",
        "Refund Issues", "Shipping Issues", "Order Issues", "Complaint Issues", "Quality Issues", "Service Issues",
        "Tracking Issues", "Negative Feedback", "Tech Support", "Refund Problems", "Shipping Problems",
        "Product Defects", "Payment Problems", "Service Complaints", "Product Complaints", "Website Issues",
        "Order Problems", "Customer Problems", "Refund Delays", "Shipping Delays", "Product Returns",
    ]

    group_mapping = {
        "Payment Issues": ["Payment Issue", "Refund Request"],
        "Delivery Issues": ["Delivery Delay", "Shipping Damage"],
        "Product Issues": ["Product Quality", "Wrong Item Received", "Product Not as Described", "Product Defects"],
        "Account Issues": ["Account Access Issue", "Order Cancellation", "Missing Items"],
        "Customer Support Issues": ["Customer Service", "Complaint Issues", "Tech Support"],
        "Refund Issues": ["Refund Problems", "Refund Delays"],
        "Shipping Issues": ["Shipping Problems", "Shipping Delays"],
        "Product Complaints": ["Product Returns"],
        "Service Complaints": ["Service Issues"],
        "Order Issues": ["Order Problems", "Order Tracking Problem"],
        "Negative Feedback": ["Negative Feedback"],
        "Website Issues": ["Website Bugs", "Order Tracking Problem"]
    }

    X_new_complaint = [
        complaint
    ]

    y_pred_new_complaint = loaded_model.predict(X_new_complaint)

    y_pred_labels = []
    for label_set in y_pred_new_complaint:
        predicted_labels = []
        
        for j in range(len(label_set)):
            try:
                if label_set[j] == 1:
                    predicted_labels.append(categories[j])
            except:
                pass
        for group, group_categories in group_mapping.items():
            if all(categories.index(cat) in [i for i, x in enumerate(label_set) if x == 1] for cat in group_categories):
                predicted_labels.append(group)

        y_pred_labels = predicted_labels

    return y_pred_labels
