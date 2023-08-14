from django.urls import path 
from .views import upload_payment
from .views import payment_list
from .views import payment_details_view


urlpatterns = [
    path("payment_/upload/", upload_payment, name= "upload_payment"),
    path("payment_/list/", payment_list, name= "payment__list"),
    path("payment_/<int:id>/",payment_details_view,name="payment_details_view")
]



# Check the File Path: Make sure that the file views.py exists in the payment package or module in the correct location within your project directory.

# Check Function or Module Name: Verify that the name 'upload_payment' is indeed a function or module defined in the views.py file.

# Check for Typos: Ensure that there are no typos in the import statement or the function/module name. Python is case-sensitive, so make sure the case matches exactly.

# Circular Imports: Circular imports can sometimes cause issues. Make sure there's no circular import relationship between modules.

# Check Other Imports: If the upload_payment function/module has its own dependencies, make sure those dependencies are properly installed and imported.

# Check Virtual Environment: Ensure that you are working within the correct virtual environment and that all required packages are installed within it.

# Check Django Version: Ensure that you are using a compatible version of Django with your project.

# Clear Compiled Files: If the error persists, try deleting any compiled .pyc or .pyo files that might be present in your project directory.

# Update Dependencies: Update your project's dependencies to the latest versions. Use a requirements.txt file to manage your dependencies and their versions.

# Review Recent Changes: If the error started occurring after you made changes to your code, review those changes to identify any potential sources of the problem.

# Check views.py: Open the views.py file in the payment package and verify that the upload_payment function/module is defined correctly.

# Check Import Statements: In your views.py file, make sure that the function/module you're trying to import is actually defined and named correctly.

