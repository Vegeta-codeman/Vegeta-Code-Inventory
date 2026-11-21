#remeber "pip install paramiko" in bash

import paramiko

#定义基础ssh的参数
def ssh_connect(hostname, username, password, port=22):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
    ssh.connect(hostname, port, username, password)
    return ssh

#定义批量下发逻辑
def batch_execute_commands(ssh, commands):
    results = []
    for command in commands:
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode('utf-8')
        error = stderr.read().decode('utf-8')
        results.append((command, output, error))
    return results

#添加错误处理和日志记录功能:

import logging

logging.basicConfig(level=logging.INFO)

def safe_execute_commands(ssh, commands):
    results = []
    for command in commands:
        try:
            stdin, stdout, stderr = ssh.exec_command(command)
            output = stdout.read().decode('utf-8')
            error = stderr.read().decode('utf-8')
            if error:
                logging.error(f"Command failed: {command}\nError: {error}")
            results.append((command, output, error))
        except Exception as e:
            logging.error(f"Execution error: {e}")
        return results

#实现配置vlan和端口的代码:

def configure_vlan_and_port(ssh, vlan_id, port):
    commands = [
        f"vlan {vlan_id}",
        f"port GigabitEthernet0/0/{port}",
        "port link-type access",
        f"port default vlan {vlan_id}"
    ]
    return safe_execute_commands(ssh, commands)