import pprint
import subprocess


def get_wifi_passwords():
    """get cached Windows wifi passwords
    
    https://www.phillipsj.net/posts/executing-powershell-from-python/
    https://www.delftstack.com/howto/powershell/powershell-utf-8-encoding-chcp-65001/
    https://ismailtasdelen.medium.com/netsh-wlan-show-profiles-select-string-de088162fce9
    """
    command = '(netsh wlan show profiles) | Select-String "\:(.+)$" | %{$name=$_.Matches.Groups[1].Value.Trim(); $_} | %{(netsh wlan show profile name="$name" key=clear)}  | Select-String "Key Content\W+\:(.+)$" | %{$pass=$_.Matches.Groups[1].Value.Trim(); $_} | %{[PSCustomObject]@{ PROFILE_NAME=$name;PASSWORD=$pass }} | Format-Table -AutoSiz'
    response = subprocess.check_output(["powershell", "-Command", command])
    lines = response.decode('Windows-1252').splitlines()
    pattern = 'PASSWORD'
    for index, line in enumerate(lines):
        if pattern in line:
            pattern_index = line.find(pattern)
            pattern_line_index = index
            break
    else:
        print('[x] wrong response')
        return {}
    lines = lines[pattern_line_index+2:]
    wifi_dict = {line[:pattern_index].rstrip():line[pattern_index:].rstrip() for line in lines if line.strip()}
    return wifi_dict
    
    
if __name__ == "__main__":
    wifi_dict = get_wifi_passwords()
    pprint.pprint(wifi_dict)
    
    