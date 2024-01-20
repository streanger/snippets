import os
import re
import itertools
from termcolor import colored

EXAMPLE_TEXT = r"""
\Microsoft\Windows\AppID\                        PolicyConverter                       Disabled
\Microsoft\Windows\AppID\                        VerifiedPublisherCertStoreCheck       Ready
\Microsoft\Windows\Application Experience\       PcaPatchDbTask                        Ready
\Microsoft\Windows\Application Experience\       StartupAppTask                        Disabled
\Microsoft\Windows\ApplicationData\              appuriverifierdaily                   Ready
\Microsoft\Windows\ApplicationData\              appuriverifierinstall                 Ready
\Microsoft\Windows\ApplicationData\              CleanupTemporaryState                 Ready
\Microsoft\Windows\ApplicationData\              DsSvcCleanup                          Ready
\Microsoft\Windows\AppListBackup\                Backup                                Disabled
\Microsoft\Windows\AppListBackup\                BackupNonMaintenance                  Ready
\Microsoft\Windows\AppxDeploymentClient\         Pre-staged app cleanup                Disabled
\Microsoft\Windows\Autochk\                      Proxy                                 Ready
\Microsoft\Windows\BitLocker\                    BitLocker Encrypt All Drives          Ready
\Microsoft\Windows\BitLocker\                    BitLocker MDM policy Refresh          Ready
\Microsoft\Windows\Bluetooth\                    UninstallDeviceTask                   Ready
\Microsoft\Windows\BrokerInfrastructure\         BgTaskRegistrationMaintenanceTask     Disabled
\Microsoft\Windows\CertificateServicesClient\    UserTask                              Ready
\Microsoft\Windows\CertificateServicesClient\    UserTask-Roam                         Disabled
\Microsoft\Windows\Chkdsk\                       ProactiveScan                         Ready
\Microsoft\Windows\Chkdsk\                       SyspartRepair                         Ready
"""

def highlight(text, word, color=None, case=True):
    """highlight all occurances of specified word in text, by coloring its background. Rest of the text stays unchanged.

    requires:
        pip install termcolor
        from termcolor import colored

    on Windows also:
        import os
        os.system('color')
    """
    if color is None:
        color = 'white'

    if case:
        pattern = re.compile(word)
        text_to_process = text
    else:
        pattern = re.compile(word.lower(), re.IGNORECASE)
        text_to_process = text.lower()

    indexes = [index for item in re.finditer(pattern, text_to_process) for index in item.span()]
    indexes = list(itertools.chain([0], indexes, [len(text)]))
    indexes = [indexes[n:n+2] for n in range(0, len(indexes)-1, 1)]
    text_chunks = [
        text[slice(*start_stop)] if not (val%2)
        else colored(text[slice(*start_stop)], color, None, ['reverse'])
        for val, start_stop in enumerate(indexes)
    ]
    highlighted_text = ''.join(text_chunks)
    return highlighted_text


if __name__ == "__main__":
    if os.name == 'nt':
        os.system('color')

    output = highlight(text=EXAMPLE_TEXT, word='Ready', color='green', case=False)
    output = highlight(text=output, word='Disabled', color='red', case=False)
    output = highlight(text=output, word='Microsoft', color='cyan', case=False)
    print(output)
