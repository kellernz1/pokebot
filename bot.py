import discord
from discord.ext import commands
import requests
import random
import asyncio
import sqlite3

# --- CONFIGURAÇÃO INICIAL ---
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# --- BANCO DE DADOS (SQLite) ---
def iniciar_db():
    conn = sqlite3.connect('pokemon_bot.db')
    cursor = conn.cursor()
    # Cria a tabela se ela não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jogadores (
            user_id TEXT PRIMARY KEY,
            username TEXT,
            pontos INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def adicionar_pontos(user_id, username, quantidade):
    conn = sqlite3.connect('pokemon_bot.db')
    cursor = conn.cursor()
    # Tenta inserir o usuário, se já existir, apenas soma os pontos
    cursor.execute('''
        INSERT INTO jogadores (user_id, username, pontos)
        VALUES (?, ?, ?)
        ON CONFLICT(user_id) DO UPDATE SET 
            pontos = pontos + ?,
            username = ?
    ''', (str(user_id), username, quantidade, quantidade, username))
    conn.commit()
    conn.close()

# --- LÓGICA POKÉMON ---
def obter_pokemon_aleatorio():
    pokemon_id = random.randint(1, 151) # Limitado aos 151 originais para facilitar
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        return dados['name'], dados['sprites']['other']['official-artwork']['front_default']
    return None, None

@bot.command(name='pokemon')
async def pokemon(ctx):
    nome_correto, imagem_url = obter_pokemon_aleatorio()
    if not nome_correto: return

    embed = discord.Embed(title="Quem é esse Pokémon?", color=discord.Color.gold())
    embed.set_image(url=imagem_url)
    await ctx.send(embed=embed)

    def check(msg):
        return msg.channel == ctx.channel and msg.content.lower() == nome_correto.lower()

    try:
        vencedor = await bot.wait_for('message', check=check, timeout=30.0)
        # ADICIONANDO PONTOS (Fase 2)
        adicionar_pontos(vencedor.author.id, vencedor.author.name, 1)
        
        await ctx.send(f"🎉 **{vencedor.author.display_name}** acertou e ganhou 1 ponto! É o **{nome_correto.capitalize()}**!")
    except asyncio.TimeoutError:
        await ctx.send(f"⏰ Tempo esgotado! Era o **{nome_correto.capitalize()}**.")

# --- COMANDO DE RANKING ---
@bot.command(name='ranking')
async def ranking(ctx):
    conn = sqlite3.connect('pokemon_bot.db')
    cursor = conn.cursor()
    cursor.execute('SELECT username, pontos FROM jogadores ORDER BY pontos DESC LIMIT 5')
    top_jogadores = cursor.fetchall()
    conn.close()

    if not top_jogadores:
        return await ctx.send("O ranking ainda está vazio. Comece a jogar com !pokemon!")

    embed = discord.Embed(title="🏆 Top 5 Treinadores Pokémon", color=discord.Color.blue())
    for i, (nome, pontos) in enumerate(top_jogadores, 1):
        embed.add_field(name=f"{i}º Lugar", value=f"{nome} - {pontos} pontos", inline=False)
    
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    iniciar_db() # Cria o banco de dados assim que o bot liga
    print(f'Tudo pronto! Banco de dados iniciado e bot online como {bot.user.name}')

TOKEN = 'YOUR_TOKEN_HERE'
bot.run(TOKEN)

