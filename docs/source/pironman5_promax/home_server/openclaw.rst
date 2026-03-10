.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _promax_openclaw_5_promax:

.. start_using_openclaw

Using OpenClaw
========================================

**What is OpenClaw?**

Think of it as an upgraded version of ChatGPT. While traditional chatbots can only talk (generate text), OpenClaw can take action. It understands your natural language instructions and can actually perform operations on your computer, such as running commands, managing files, and calling various tools.

Here are some fantastic application scenarios:

* **Personal All-around Assistant:** Let it help you manage your schedule, set reminders, and track tasks. You just need to tell it in a chat app (like Telegram, WhatsApp), and it will remember and execute.
* **Automation "Glue":** It can act as a binder for your various services. For example, you can have it monitor a website for price changes. Once a price drop is detected, it can automatically trigger an n8n automation workflow to send you an email notification.
* **Dedicated Development Assistant:** Have it help you manage servers, run scripts, and check logs. You can simply say, "Check the system load for me," and it can SSH into your server, execute the command, and return the results.
* **Hardware "Playmate":** This is a very interesting use case. You can have OpenClaw control hardware connected to a Raspberry Pi. For example, a developer used it to control a robotic vacuum cleaner with a mechanical arm, or even had it help analyze racing simulator data and display it on an LED screen. The official Raspberry Pi team even used it to build an automatic photo booth for a wedding, just through conversation, without writing a single line of code!

**Why install openclaw on a Raspberry Pi?**

Installing it on a Raspberry Pi has two main advantages:

* **Security Isolation:** OpenClaw requires higher system permissions, which poses a risk on a primary computer. Using a Raspberry Pi as a dedicated device is like giving it a "sandbox"; even if something goes wrong, it won't affect your main system.
* **24/7 Online:** The Raspberry Pi has extremely low power consumption, allowing it to stay on all the time, ready to execute tasks at any moment.

----------------------------------------------------------------

Quick Start OpenClaw
------------------------------

If you want to experience the power of OpenClaw as quickly as possible, use this method. It will automatically install and launch an interactive setup wizard.

1.  Open the terminal on your Raspberry Pi and run the following command directly. This command downloads the installation script from the official website and executes it:

    .. code-block:: bash

       curl -fsSL https://openclaw.ai/install.sh | bash
   
    .. note:: Because new versions are updated rapidly, it's normal if your installation steps differ slightly.

2.  The script will automatically download and install OpenClaw.

    .. image:: img/openclaw/install_open_claw.png


3.  You will then see a security prompt asking if you trust OpenClaw. Once you are sure it is safe and reliable, use the arrow keys to navigate to "Yes" and press Enter.

    .. image:: img/openclaw/security_open_claw.png


4.  Select Quick Start, and then press Enter.

    .. image:: img/openclaw/quickstart_open_claw.png

5.  Select your Model, and then press Enter. Here we use OpenAI as an example.

    .. image:: img/openclaw/model_provider_open_claw.png

6.  Select OpenAI API Key.

    .. image:: img/openclaw/api_key_open_claw.png

7.  Paste API key now.

    .. image:: img/openclaw/paste_api_key_open_claw.png

.. |link_openai_platform| raw:: html

    <a href="https://platform.openai.com/settings/organization/api-keys" target="_blank">OpenAI Platform</a>

8.  Go to |link_openai_platform| and log in. On the **API keys** page, click **Create new secret key**.

    .. image:: img/openclaw/llm_openai_create.png

9.  Fill in the details (Owner, Name, Project, and permissions if needed), then click **Create secret key**.

    .. image:: img/openclaw/llm_openai_create_confirm.png

10. Once the key is created, copy it right away — you won't be able to see it again. If you lose it, you'll need to generate a new one.

    .. image:: img/openclaw/llm_openai_copy.png

11. Paste the key into the OpenCLaw configuration.

    .. image:: img/openclaw/paste_api_key_enter_open_claw.png

12. Select the Model you want to use. In this example, we will use **Keep current**.

    .. image:: img/openclaw/model_config_open_claw.png

13. Next is the channel selection. Channels refer to the communication services supported by OpenClaw, such as Telegram, WhatsApp, Discord, and more. Use the down arrow key to select the "Skip for now" option, then press Enter.

    .. image:: img/openclaw/channel_open_claw.png

14. Next, you will be prompted to configure skills immediately. Select "Yes" and press Enter.

    .. image:: img/openclaw/config_skill_open_claw.png

15. Install the skills you need. In the following example, we select the "Skip for now" option (press the spacebar to select), then press Enter.

    .. image:: img/openclaw/install_skill_open_claw.png


16. Next are Hooks; we will check "command-logger" and "session-memory".

    .. image:: img/openclaw/hooks2_open_claw.png


17. The installation is now complete. You can start OpenClaw by Selecting "Hatch in TUI" and pressing Enter.

   .. image:: img/openclaw/hatch_open_claw.png


.. note:: 
   
   You can start OpenClaw by entering the following command:

    .. code-block:: bash

       openclaw tui

   And You can press ctrl+c twice to exit the tui interface.




-----------------------------------------------------

.. end_using_openclaw

Making OpenClaw Operate the Pironman5 Pro MAX
----------------------------------------------

To enable OpenClaw to operate the Pironman5 Pro MAX, we need to install the Pironman5 Pro MAX skill.

1.  Ensure you have already installed the Pironman5 Pro MAX. If not, please refer to :ref:`promax_download_pironman5_module`.

2.  Run the following command in the terminal:

    .. code-block:: bash

       mkdir -p ~/.openclaw/skills && rsync -av --delete ~/pironman5/skill/pironman5-promax-skill/ ~/.openclaw/skills/pironman5-promax-skill/

3.  You can now operate the Pironman5 Pro MAX in ``openclaw tui``. Try sending commands in the TUI, such as attempting to turn on the LED lights on the case, change their color, or have the camera take a photo.

   .. note:: If OpenClaw is still unable to recognize the skill you imported, please remind it to rsync.

-------------------------------------------------------------

Interacting with Voice
----------------------------------------------------

The Pro MAX case has a built-in microphone and speaker, so you can use the Pironman5 Pro MAX to interact with OpenClaw via voice. To achieve this, you need to install the ``sunfounder-voice-assistant`` package.

The ``sunfounder-voice-assistant`` package provides the necessary libraries and tools for operating the Pironman 5 Pro MAX hardware.

Run the following installation command:

.. code-block:: bash


   sudo apt install portaudio19-dev
   sudo pip install --break git+https://github.com/sunfounder/sunfounder-voice-assistant.git


Here you will explore text-to-speech (TTS), speech-to-text (STT), and large language models (LLMs) to make your Pironman 5 Pro MAX talk, listen, and even chat with you like a smart robot.

Then, run the following example:

.. code-block:: bash

   python3 ~/pironman5/openclaw_voice.py

Reboot. Then you can use the voice features of the Pironman5 Pro MAX to interact with OpenClaw. Try saying "Hi Amy" to wake it up.



-------------------------------------

**Troubleshooting**


Q. During installation, I get the error ``Error: systemctl is-enabled unavailable: Command failed: systemctl --user is-enabled openclaw-gateway.service``. What should I do?

A. You can ignore this for now, but you might encounter issues in the next steps. Please refer to them one by one at that time.


Q. When I run ``openclaw tui``, I get the error ``-bash: openclaw: command not found``. What should I do?

A. Execute the following command:

    .. code-block:: bash

       echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.bashrc
       source ~/.bashrc

    You should now be able to start the tui interface with ``openclaw tui``.



Q. In ``openclaw tui``, I encounter ``not connected to gateway — message not sent`` or the message ``gateway disconnected: closed``.

A. This is because your OpenClaw Gateway service is not started. Open another terminal and execute the following command to start the OpenClaw Gateway:

    .. code-block:: bash

       openclaw gateway

    Then restart ``openclaw tui``, and you can use it directly.

Q. I want to set the OpenClaw Gateway service to run in the background / start automatically on boot. How do I do that?

A. Execute the following commands:

    1. Create the ``~/.config/systemd/user`` directory:

    .. code-block:: bash

       mkdir -p ~/.config/systemd/user


    2. Create the ``openclaw-gateway.service`` file:

    .. code-block:: bash

       cat > ~/.config/systemd/user/openclaw-gateway.service << EOF
       [Unit]
       Description=OpenClaw Gateway
       After=network.target

       [Service]
       Type=simple
       ExecStart=$HOME/.npm-global/bin/openclaw gateway run
       Restart=on-failure
       RestartSec=10
       Environment="PATH=$HOME/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin"
       Environment="NODE_ENV=production"

       [Install]
       WantedBy=default.target
       EOF


    3. Then reload the systemd configuration:

    .. code-block:: bash

       systemctl --user daemon-reload

    4. Start the service:

    .. code-block:: bash

       systemctl --user start openclaw-gateway

    At this point, restart ``openclaw tui``, and you can use it directly.

    5. Enable it to start on boot:

    .. code-block:: bash

       systemctl --user enable openclaw-gateway


Q. My OpenClaw can not operate the system, what should I do?

A. A newly installed OpenClaw may not have permission to operate your Raspberry Pi system by default; it can only chat. We need to manually configure the permissions.

    1.  Open the OpenClaw configuration file:

        .. code-block:: bash

        nano ~/.openclaw/openclaw.json

    2.  Find the ``tools`` option and change the ``profile`` from ``message`` to ``coding``.

        .. code-block:: json

        "tools": {
            "profile": "coding"
        },

    3.  Save and exit.

    4.  Enter the following command in the terminal to restart the OpenClaw Gateway:

        .. code-block:: bash

        openclaw gateway restart

    Now, OpenClaw should have read and write permissions and be able to operate your Raspberry Pi system.