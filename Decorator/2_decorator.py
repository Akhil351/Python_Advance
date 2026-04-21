def login_required(func):
    def wrapper():
        user_logged_in = True  # change to False to test

        if user_logged_in:
            return func()
        else:
            print("Access Denied. Please login.")

    return wrapper


@login_required
def view_dashboard():
    print("Welcome to Dashboard")


view_dashboard()
