.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _control_commands_dashboard_promax:

5. コマンドまたはダッシュボードによる制御
=======================================================

``pironman5`` モジュールが正常にインストールされると、 ``pironman5.service`` は再起動時に自動的に起動します。

Pironman 5 Pro MAX は、コマンドを使用するか、 ``http://<ip>:34001`` のウェブページからダッシュボードにアクセスすることで、監視および制御できます。

.. .. note::

..     * **Home Assistant** システムの場合、Pironman 5 Pro MAX の監視と制御は、 ``http://<ip>:34001`` のウェブページを開いてダッシュボード経由でのみ行えます。

.. * **Batocera.linux** システムの場合、Pironman 5 Pro MAX の監視と制御はコマンド経由でのみ行えます。設定を変更した場合は、 ``pironman5 restart`` を使用してサービスを再起動する必要があることに注意してください。


.. toctree::
    :maxdepth: 1

    control_with_dashboard 
    control_with_commands
    conf_display