# 📜 Who's That Pokémon? - Discord Bot

An interactive and fun Discord mini-game bot inspired by the classic "Who's That Pokémon?" segment. Test your Pokémon knowledge, compete with friends, and climb the server ranking!

---

## 🚀 Features

- 🎮 **Interactive Game Loop**  
  Use `!pokemon` to start a round. The bot fetches a random Pokémon from the PokéAPI and waits for the correct answer.

- 🏆 **Global Ranking System**  
  A built-in **SQLite** database stores user scores, allowing players to see the Top 5 trainers using the `!ranking` command.

- 💡 **Dynamic Hints**  
  If a round is active, the bot provides the first letter and the length of the Pokémon's name to help players.

- 🌐 **Real-time Data**  
  No local images needed! The bot consumes the [PokéAPI](https://pokeapi.co/) to get up-to-date data and official artworks.

---

## 🛠️ Technologies Used

- **Language:** Python 3.10+
- **Library:** [discord.py](https://github.com/Rapptz/discord.py)
- **API:** PokéAPI (REST)
- **Database:** SQLite3
- **Tools:** Requests (HTTP Library), Difflib (Fuzzy Matching)

---

## 📦 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/pokemon-discord-bot.git
cd pokemon-discord-bot
```

### 2. Create a virtual environment and install dependencies

#### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
pip install discord.py requests
```

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
pip install discord.py requests
```

---

### 3. Configure the Discord Developer Portal

1. Create an application at the [Discord Developer Portal](https://discord.com/developers/applications)
2. Go to the **Bot** tab
3. Enable **Message Content Intent**
4. Copy your bot token

---

### 4. Configure and Run the Bot

Open `bot.py` and replace:

```python
TOKEN = "YOUR_TOKEN_HERE"
```

with your actual Discord bot token.

Run the bot:

```bash
python bot.py
```

---

## 🎮 Commands

| Command | Description |
|----------|-------------|
| `!pokemon` | Starts a new round with a random Pokémon image |
| `!ranking` | Displays the Top 5 players on the server |
| `!ping` | Checks if the bot is online |

---

## 🏗️ Future Improvements (Roadmap)

- [ ] 🌑 Silhouette Mode (Show only the Pokémon shadow)
- [ ] 🎚️ Difficulty Levels (Generation filters)
- [ ] 🌍 Multiple Language Support (Portuguese & Japanese names)
- [ ] 📊 Web Dashboard for rankings and statistics
- [ ] 🔊 Sound effects and battle music

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to fork this project and submit pull requests.

---

## 👨‍💻 Author

Developed with ❤️ by **Keller Nz**

---

## ⭐ Support

If you enjoyed this project, consider giving it a ⭐ on GitHub!
