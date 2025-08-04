# 🔁 Python Reverse Shell Client

This is a simple Python-based reverse shell client that connects back to a listener (server) and provides remote shell access to the attacker's machine. It is designed for **educational purposes**, such as learning about networking, cybersecurity, and penetration testing.

> ⚠️ Disclaimer: This tool is intended **only for ethical hacking and authorized testing**. Do not use it against systems you do not own or have explicit permission to test.

---

## 📜 Features

- Connects to a remote host over TCP
- Executes shell commands sent by the server
- Sends back the command output or error
- Supports continuous command execution until terminated

---

## 📂 Files

- `client.py` — The reverse shell client script.

---

## 🚀 How It Works

1. The client connects to a predefined host and port.
2. It waits for shell commands from the server.
3. When a command is received:
   - It's executed using the system shell.
   - Output (or errors) is sent back to the server.
4. The session can be terminated by sending `exit`.

---

## 🔧 Usage

### 1. Start a listener on the attacker's machine (server):

```bash
nc -lvp 9000
