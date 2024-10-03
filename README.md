# Automated Messenger Scheduling Assisant

This is a Python tool that helps that automated send messenge to somebody via Messenger. With this tool, you can easily send messenges automatically.

## Getting Started

### 1. Environment Setup
Follow these steps to set up your environment:

1. **Create a Python virtual environment:**
    ```sh
    cd <path-to-venv-directory>
    python -m venv venv
    ```
2. **Activate the virtiual environment:**  
    **$\bullet$ On Windows:**
    ```sh
    venv/Scripts/activate
    ```
    **$\bullet$ On Linux or macOS:**
    ```sh
    source venv/bin/activate
    ```
3. **Install the required package:**
    ```sh
    cd <path-to-repository-directory>
    pip install -r requirement.txt
    ```
### 2. Configuration
1. **Copy config_sample.py to config.py:
    ```sh
    cp config_sample.py config.py
    ```
2. **Edit config.py and set the parameters such as urls, send_time, messenge according to your requirements.**

### 3. Sending the Messenge
1. **Use messenger_scheduling.py to send the messenge:**
    ```sh
    python messenger_scheduling.py
    ```

## File Structure
**$\bullet$ requirements.txt:** Lists the Python package required for the tool.  
**$\bullet$ config_sample.py:** Provide a sample configuration. You need to copy it to config.py and customize the parameters.  
**$\bullet$ messenger_scheduling.py:** The main script for sending Messenger messages.

## Notes
This is my first small project, created to help me make a reservation at a café for the girl I like. Due to my limited experience, there may be some shortcomings in this repository. I would greatly appreciate any feedback or suggestions.

## FAQ

## Contact
If you have any questions or suggestion, feel free to reach out.
