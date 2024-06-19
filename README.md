# Discord Bot Dashboard API Tool

Welcome to the Discord Bot Dashboard API Tool. Here you can manage your Discord server using a discord bot and simple web interface.




## Installation

- Download site from https://github.com/freeutka-cmd/dashboard-api/releases
- Export all files to your bot directory
- Open app.py, and replace DISCORD_BOT_TOKEN with your bot token.
- Run command
```py
pip install -r requirements.txt
```
- Run command
```py
python app.py
```
- In cmd shows the site ip, standart is ```http://127.0.0.1:5000/``` or ```http://localhost:5000/```
- Enjoy!
    
## How to Use

- **View Channels:** Send a GET request to ```/channels?guild_id=YOUR_GUILD_ID```. (Works only where there is a bot)
- **Create Channel:** Send a POST request to ```/channels``` with JSON data: ```{"guild_id": "YOUR_GUILD_ID", "channel_name": "CHANNEL_NAME"}```. (Works only where there is a bot)
- **Delete Channel:** Send a DELETE request to ```/channels/CHANNEL_ID```. (Works only where there is a bot)
- **View Roles:** Send a GET request to ```/roles?guild_id=YOUR_GUILD_ID```. (Works only where there is a bot)
- **Create Role:** Send a POST request to ```/roles``` with JSON data: ```{"guild_id": "YOUR_GUILD_ID", "role_name": "ROLE_NAME"}```. (Works only where there is a bot)
- **Delete Role:** Send a DELETE request to ```/roles/ROLE_ID```. (Works only where there is a bot)
- **View Members:** Send a GET request to ```/members?guild_id=YOUR_GUILD_ID```. (Works only where there is a bot)
- **Kick Member:** Send a POST request to ```/members/MEMBER_ID/kick?guild_id=YOUR_GUILD_ID```. (Works only where there is a bot)
- **Ban Member:** Send a POST request to ```/members/MEMBER_ID/ban``` with JSON data: ```{"reason": "REASON"}```. (Works only where there is a bot)
- **Send Message:** Send a POST request to ```/messages``` with JSON data: ```{"channel_id": "CHANNEL_ID", "message": "MESSAGE_CONTENT"}```. (Works only where there is a bot)

## Examples

#### View Channels

`curl -X GET "http://localhost:5000/channels?guild_id=YOUR_GUILD_ID"`

#### Create a Channel

`curl -X POST http://localhost:5000/channels -H "Content-Type: application/json" -d '{"guild_id": "YOUR_GUILD_ID", "channel_name": "new-channel"}'`

#### Delete a Channel

`curl -X DELETE http://localhost:5000/channels/CHANNEL_ID`

#### View Roles

`curl -X GET "http://localhost:5000/roles?guild_id=YOUR_GUILD_ID"`

#### Create a Role

`curl -X POST http://localhost:5000/roles -H "Content-Type: application/json" -d '{"guild_id": "YOUR_GUILD_ID", "role_name": "new-role"}'`

#### Delete a Role

`curl -X DELETE "http://localhost:5000/roles/ROLE_ID?guild_id=YOUR_GUILD_ID"`

#### View Members

`curl -X GET "http://localhost:5000/members?guild_id=YOUR_GUILD_ID"`

#### Kick a Member

`curl -X POST "http://localhost:5000/members/MEMBER_ID/kick?guild_id=YOUR_GUILD_ID"`

#### Ban a Member

`curl -X POST http://localhost:5000/members/MEMBER_ID/ban -H "Content-Type: application/json" -d '{"reason": "Violation of rules"}'`

#### Send a Message

`curl -X POST http://localhost:5000/messages -H "Content-Type: application/json" -d '{"channel_id": "CHANNEL_ID", "message": "Hello, world!"}'`


## API Endpoints

| Endpoint | Method     | Description                |
| :-------- | :------- | :------------------------- |
| `/channels` | `GET` | List all channels in a guild. |
| `/channels` | `POST` | Create a new channel in a guild. |
| `/channels/<channel_id>` | `DELETE` | Delete a channel. |
| `/roles` | `GET` | List all roles in a guild. |
| `/roles` | `POST` | Create a new role in a guild. |
| `/roles/<role_id>` | `DELETE` | Delete a role. |
| `/members` | `GET` | List all members in a guild. |
| `/members/<member_id>/kick` | `POST` | Kick a member from a guild. |
| `/members/<member_id>/ban` | `POST` | Ban a member from a guild. |
| `/messages` | `POST` | Send a message to a channel.y |


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)

[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Feedback

If you have any feedback, please reach out to us at desingfreeutka@gmail.com

