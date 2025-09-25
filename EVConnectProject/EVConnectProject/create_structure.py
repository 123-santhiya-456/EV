import os

# Define the root directory
root = 'evconnect'

# Function to create directory if it doesn't exist
def create_dir(path):
    os.makedirs(path, exist_ok=True)

# Function to create an empty file
def create_file(path):
    with open(path, 'w') as f:
        pass  # Creates an empty file

# Create root directory
create_dir(root)

# Client section
client = os.path.join(root, 'client')
create_dir(client)

# client/public
public = os.path.join(client, 'public')
create_dir(public)
create_file(os.path.join(public, 'index.html'))
create_file(os.path.join(public, 'favicon.ico'))
create_file(os.path.join(public, 'manifest.json'))

# client/src
src = os.path.join(client, 'src')
create_dir(src)

# src/components
components = os.path.join(src, 'components')
create_dir(components)

# components/ChargingAssistance
charging_assist = os.path.join(components, 'ChargingAssistance')
create_dir(charging_assist)
create_file(os.path.join(charging_assist, 'ChargingMap.tsx'))
create_file(os.path.join(charging_assist, 'ChargingList.tsx'))
create_file(os.path.join(charging_assist, 'ChargingCard.tsx'))
create_file(os.path.join(charging_assist, 'index.ts'))

# components/Community
community = os.path.join(components, 'Community')
create_dir(community)
create_file(os.path.join(community, 'ChatWindow.tsx'))
create_file(os.path.join(community, 'ChatBot.tsx'))
create_file(os.path.join(community, 'PeerChat.tsx'))
create_file(os.path.join(community, 'MessageBubble.tsx'))
create_file(os.path.join(community, 'index.ts'))

# components/MapView
map_view = os.path.join(components, 'MapView')
create_dir(map_view)
create_file(os.path.join(map_view, 'MapView.tsx'))
create_file(os.path.join(map_view, 'UserMarker.tsx'))
create_file(os.path.join(map_view, 'index.ts'))

# components/layout
layout = os.path.join(components, 'layout')
create_dir(layout)
create_file(os.path.join(layout, 'Navbar.tsx'))
create_file(os.path.join(layout, 'Sidebar.tsx'))
create_file(os.path.join(layout, 'Footer.tsx'))
create_file(os.path.join(layout, 'index.ts'))

# components/ui
ui = os.path.join(components, 'ui')
create_dir(ui)
create_file(os.path.join(ui, 'Button.tsx'))
create_file(os.path.join(ui, 'Card.tsx'))
create_file(os.path.join(ui, 'Modal.tsx'))
create_file(os.path.join(ui, 'index.ts'))

# src/pages
pages = os.path.join(src, 'pages')
create_dir(pages)
create_file(os.path.join(pages, 'Home.tsx'))
create_file(os.path.join(pages, 'Charging.tsx'))
create_file(os.path.join(pages, 'Community.tsx'))
create_file(os.path.join(pages, 'Map.tsx'))
create_file(os.path.join(pages, 'NotFound.tsx'))

# src/services
services = os.path.join(src, 'services')
create_dir(services)
create_file(os.path.join(services, 'firebase.ts'))
create_file(os.path.join(services, 'authService.ts'))
create_file(os.path.join(services, 'chatService.ts'))
create_file(os.path.join(services, 'chargingService.ts'))
create_file(os.path.join(services, 'locationService.ts'))

# src/hooks
hooks = os.path.join(src, 'hooks')
create_dir(hooks)
create_file(os.path.join(hooks, 'useAuth.ts'))
create_file(os.path.join(hooks, 'useChat.ts'))
create_file(os.path.join(hooks, 'useLocation.ts'))
create_file(os.path.join(hooks, 'useFirestore.ts'))

# src/types
types = os.path.join(src, 'types')
create_dir(types)
create_file(os.path.join(types, 'chat.ts'))
create_file(os.path.join(types, 'charging.ts'))
create_file(os.path.join(types, 'location.ts'))
create_file(os.path.join(types, 'index.ts'))

# src/utils
utils = os.path.join(src, 'utils')
create_dir(utils)
create_file(os.path.join(utils, 'formatDate.ts'))
create_file(os.path.join(utils, 'geoUtils.ts'))
create_file(os.path.join(utils, 'index.ts'))

# src files
create_file(os.path.join(src, 'App.tsx'))
create_file(os.path.join(src, 'index.tsx'))
create_file(os.path.join(src, 'routes.tsx'))

# src/styles
styles = os.path.join(src, 'styles')
create_dir(styles)
create_file(os.path.join(styles, 'index.css'))
create_file(os.path.join(styles, 'tailwind.css'))

# client files
create_file(os.path.join(client, 'package.json'))
create_file(os.path.join(client, 'tsconfig.json'))
create_file(os.path.join(client, 'tailwind.config.js'))

# Server section
server = os.path.join(root, 'server')
create_dir(server)

# server/chatbot
chatbot = os.path.join(server, 'chatbot')
create_dir(chatbot)
create_file(os.path.join(chatbot, 'chatbot_app.py'))
create_file(os.path.join(chatbot, 'chat.html'))
create_file(os.path.join(chatbot, 'chat_log.txt'))

# server/chat_system
chat_system = os.path.join(server, 'chat_system')
create_dir(chat_system)

# chat_system/pycache_ (as per structure, though typically ignored)
pycache = os.path.join(chat_system, 'pycache_')
create_dir(pycache)

# chat_system/node_modules (empty dir, as deps are installed later)
node_modules = os.path.join(chat_system, 'node_modules')
create_dir(node_modules)

# routes
routes = os.path.join(chat_system, 'routes')
create_dir(routes)
create_file(os.path.join(routes, 'stations.js'))
create_file(os.path.join(routes, 'chat.js'))

# socket
socket = os.path.join(chat_system, 'socket')
create_dir(socket)
create_file(os.path.join(socket, 'socket_handler.py'))
create_file(os.path.join(socket, 'index.js'))

# env
env = os.path.join(chat_system, 'env')
create_dir(env)

# utils
utils_server = os.path.join(chat_system, 'utils')
create_dir(utils_server)

# auth
auth = os.path.join(chat_system, 'auth')
create_dir(auth)

# chat_system files (as per structure)
create_file(os.path.join(chat_system, 'Home.tsx'))
create_file(os.path.join(chat_system, 'settings.tsx'))
create_file(os.path.join(chat_system, 'app.ts'))
create_file(os.path.join(chat_system, 'index.css'))
create_file(os.path.join(chat_system, 'index.html'))
create_file(os.path.join(chat_system, 'package-lock.json'))
create_file(os.path.join(chat_system, 'package.json'))
create_file(os.path.join(chat_system, 'README.md'))
create_file(os.path.join(chat_system, 'server.js'))

# server files
create_file(os.path.join(server, 'package.json'))
create_file(os.path.join(server, '.env'))

# Root files
create_file(os.path.join(root, 'README.md'))
create_file(os.path.join(root, '.gitignore'))

print(f"Folder structure for '{root}' has been created successfully!")