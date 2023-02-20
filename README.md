# Upload Image App


## To run the application:

- Open a Bash console in the main directory
- Type the command "source virt/Scripts/activate"
- Navigate to the upload_image_app directory using the command "cd upload_image_app"
- Start the server by typing "python manage.py runserver"
- Information will be displayed in the console and in the line "Starting development server at" a URL will be provided to launch the application page.

On the website, there are "Upload Image", "My Images", and "Login/Logout" tabs. To upload an image, you need to log in. Two accounts have been created by me: admin(Enterprise) and bob(Basic). These users are created for testing purposes.

- Login: admin, password: admin
- Login: bob, password: bobbobbob

To log in to the Django admin page, use the user account "admin". There are two models: "Accounts" and "Images". The "Images" model is responsible for saving an uploaded image to the logged-in user's account and creating two thumbnail versions of the image (200px and 400px). The "Accounts" model is responsible for assigning the appropriate account level (Basic, Premium, Enterprise) to a user.

To upload images, you need to go to the "Upload Images" tab and be logged in as a user. If you are not logged in, you will be informed about it and redirected to the login page. The same applies when you go to the "My Images" tab to view your images.
Uploading images is very simple. We select a file, confirm and click the Submit button. Then, we will be redirected to the My Images tab, where we will see all our images in 200px thumbnail size that have been uploaded. Depending on the type of account, different buttons with a reference to the image of the appropriate resolution specified in the button name will be displayed.


## Libraries used in the application.
- Django
- imagekit


## Own remarks/notes.
- During the creation of the application, other libraries were also installed in addition to those that were used: "Pillow", "requests", and others that were automatically installed during the installation of the mentioned ones.
- In the "Accounts" model, it is possible to select the same user multiple times. I tried to set it up so that the same value could be selected only once. At first, I used models.ForeignKey and set the unique=True option. Unfortunately, with this option, I could still select the same user multiple times. Additionally, during migration, a warning was displayed to use models.OneToOneField in such a case. Unfortunately, that also did not help.
- In case of a user with an Enterprise profile, they should have an option to display the image for a selected period of time. Unfortunately, this option was not implemented. I received an error about a non-existent file in the image link, even though it was correct. Temporarily, I was unable to resolve this issue.
- This project was written after two weeks of learning about the Django framework.
- In the project, there should be comments to describe the code. Unfortunately, I ran out of time.


Thank you for giving me a chance!
