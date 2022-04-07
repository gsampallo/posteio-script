# MailAPI

Script for create a list of mailbox and define the storage limit for each mailbox from a spreadsheet.
Also include an wrapper for the api of poste.io for python.

## How to install


Just clone the repository:

~~~
git clone xxxx
~~~

The xlwt and xlrd package is needed for use with spreadsheet, install this with pip:
~~~
pip install xlwt
pip install xlrd
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

## Use

First You need to provide an spreadsheet with list of the names, mail address and storage limit (mb), not fancy format needed:

|Name|Email|Size|
|----|-----|-----|
|Jhon Doe|jdoe@your_posteio_mail.com|100|

On Size use 0 for ilimited storage. In the repository you can find an [example](mails.xls).

When you has the spreadsheet with list of mailbox, to create the accounts run:
~~~
python posteio-script.py new mail.xls
~~~

If you need to update the quota of the accounts run the following command:
~~~
python posteio-script.py quota mail.xls
~~~
This last command is not working yet.

As a result you get a new spreadsheet with the mailboxes created, each of them with the password associated.


[![alt text](https://cdn.cafecito.app/imgs/cafecito_logo.svg) If you like this project, maybe you can support with a cofee](https://cafecito.app/gsampallo) 


