# MailAPI

Script for create a list of mailbox and define the storage limit for each mailbox from a spreadsheet.
Also include an wrapper for the api of poste.io for python.

## How to install


Just clone the repository:

~~~
git clone xxxx
~~~

The xlwt package is needed for use with spreadsheet, install this with pip:
~~~
pip install xlwt
~~~

## Configure credentials

On the directory where download the repository, create a configuration.json file with this content:
~~~
{
    "mail_url": "https://url_of_your_posteio_mail.com",
    "username": "admin@your_posteio_mail.com",
    "password": "password"
}
~~~

