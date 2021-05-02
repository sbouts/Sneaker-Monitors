# Sneaker Monitors
*A collection of web monitors that notify of restocks or updates on sneaker related sites through Discord Webhook*

<a href="https://www.buymeacoffee.com/yasserqureshi" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>


## Contents
* [About the Project](#about-the-project)
* [Monitors](#monitors)
* [Installation](#installation)
* [Set Up](#set-up)
* [Issues](#issues)
* [To Do](#to-do)
* [License](#license)
* [Contact](#contact)


## Installation
Ensure you have [Python 3+](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/) installed. 

To install the dependencies, use the command:
```
pip install -r requirements.txt
```

## Set Up

1. First perform the installation described in [#Installation](#installation).

2. Clone or Download the repository
    - Clone:
    ```
    git clone https://github.com/yasserqureshi1/Sneaker-Monitors.git
    ```
    - Download: Click on the green `Code` button and click on `Download ZIP`. Then unzip this folder
    
3. Start editting the `.env` file to your specifications. You will only be interacting with the ```.env``` file.
    - **Add Webhook**: Paste your Discord Webhook URL under the `WEBHOOK` variable. It should look like this:
    ```
    WEBHOOK = "https://discord.com/api/webhooks/..."
    ```
    - (Optional) **Add Proxy**: Paste your proxy under the `PROXY` variable. There are two structures:

        1. ```PROXY = "<proxy>:<port>"``` 
        2. ```PROXY = "<proxy_username>:<proxy_password>@<proxy_domain>:<port>"```
    - You can also edit other details within the `.env` file as you see fit

    
## Issues

If you find an issue, please open an issue [here](https://github.com/yasserqureshi1/Sneaker-Monitors/issues/new). 
I will respond fairly quickly and try to come up with solution.
I may ask you to provide the log file that is produced by the monitor.
It contains no personal data but may help me diagnose where the issue arises.

If you are struggling to set up the monitor you can reach out to me via Discord [here](#contact)

## License

Distributed under the MIT License. See ```LICENSE``` for more information.

## Contact

For help contact me via Discord at @TheBrownPanther2#3801
