# app.py Required.
from flask import Flask, request, jsonify, render_template, redirect, url_for
import requests

app = Flask(__name__)

# Replace it with your bot token.
DISCORD_BOT_TOKEN = 'DISCORD_BOT_TOKEN'
DISCORD_API_URL = 'https://discord.com/api/v9'

HEADERS = {
    'Authorization': f'Bot {DISCORD_BOT_TOKEN}',
    'Content-Type': 'application/json'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view_channels_form')
def view_channels_form():
    return render_template('view_channels.html')

@app.route('/view_roles_form')
def view_roles_form():
    return render_template('view_roles.html')

@app.route('/view_members_form')
def view_members_form():
    return render_template('view_members.html')

@app.route('/create_channel_form')
def create_channel_form():
    return render_template('create_channel.html')

@app.route('/delete_channel_form')
def delete_channel_form():
    return render_template('delete_channel.html')

@app.route('/create_role_form')
def create_role_form():
    return render_template('create_role.html')

@app.route('/delete_role_form')
def delete_role_form():
    return render_template('delete_role.html')

@app.route('/kick_member_form')
def kick_member_form():
    return render_template('kick_member.html')

@app.route('/ban_member_form')
def ban_member_form():
    return render_template('ban_member.html')

@app.route('/send_message_form')
def send_message_form():
    return render_template('send_message.html')

@app.route('/channels', methods=['GET'])
def list_channels():
    guild_id = request.args.get('guild_id')
    response = requests.get(f'{DISCORD_API_URL}/guilds/{guild_id}/channels', headers=HEADERS)
    return render_template('results.html', results=response.json())

@app.route('/roles', methods=['GET'])
def list_roles():
    guild_id = request.args.get('guild_id')
    response = requests.get(f'{DISCORD_API_URL}/guilds/{guild_id}/roles', headers=HEADERS)
    return render_template('results.html', results=response.json())

@app.route('/members', methods=['GET'])
def list_members():
    guild_id = request.args.get('guild_id')
    response = requests.get(f'{DISCORD_API_URL}/guilds/{guild_id}/members', headers=HEADERS)
    return render_template('results.html', results=response.json())

@app.route('/create_channel', methods=['POST'])
def create_channel():
    guild_id = request.form.get('guild_id')
    channel_name = request.form.get('channel_name')
    payload = {
        'name': channel_name,
        'type': 0
    }
    response = requests.post(f'{DISCORD_API_URL}/guilds/{guild_id}/channels', headers=HEADERS, json=payload)
    return redirect(url_for('list_channels', guild_id=guild_id))

@app.route('/delete_channel', methods=['POST'])
def delete_channel():
    channel_id = request.form.get('channel_id')
    response = requests.delete(f'{DISCORD_API_URL}/channels/{channel_id}', headers=HEADERS)
    return redirect(url_for('index'))

@app.route('/create_role', methods=['POST'])
def create_role():
    guild_id = request.form.get('guild_id')
    role_name = request.form.get('role_name')
    payload = {
        'name': role_name
    }
    response = requests.post(f'{DISCORD_API_URL}/guilds/{guild_id}/roles', headers=HEADERS, json=payload)
    return redirect(url_for('list_roles', guild_id=guild_id))

@app.route('/delete_role', methods=['POST'])
def delete_role():
    role_id = request.form.get('role_id')
    guild_id = request.form.get('guild_id')
    response = requests.delete(f'{DISCORD_API_URL}/guilds/{guild_id}/roles/{role_id}', headers=HEADERS)
    return redirect(url_for('list_roles', guild_id=guild_id))

@app.route('/kick_member', methods=['POST'])
def kick_member():
    member_id = request.form.get('member_id')
    guild_id = request.form.get('guild_id')
    response = requests.delete(f'{DISCORD_API_URL}/guilds/{guild_id}/members/{member_id}', headers=HEADERS)
    return redirect(url_for('list_members', guild_id=guild_id))

@app.route('/ban_member', methods=['POST'])
def ban_member():
    member_id = request.form.get('member_id')
    guild_id = request.form.get('guild_id')
    reason = request.form.get('reason', 'No reason provided')
    payload = {
        'delete_message_days': 0,
        'reason': reason
    }
    response = requests.put(f'{DISCORD_API_URL}/guilds/{guild_id}/bans/{member_id}', headers=HEADERS, json=payload)
    return redirect(url_for('list_members', guild_id=guild_id))

@app.route('/send_message', methods=['POST'])
def send_message():
    channel_id = request.form.get('channel_id')
    message = request.form.get('message')
    payload = {
        'content': message
    }
    response = requests.post(f'{DISCORD_API_URL}/channels/{channel_id}/messages', headers=HEADERS, json=payload)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)