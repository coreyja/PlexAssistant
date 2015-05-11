from plexapi.myplex import MyPlexUser
import argparse
from sort import Sorter

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run demo script')
    parser.add_argument('-u', '--username', help='Username for the Plex server.')
    parser.add_argument('-p', '--password', help='Password for the Plex server.')
    args = parser.parse_args()

    user = MyPlexUser.signin(args.username, args.password)

    server_name = user.servers()[0].name
    server = user.getServer(server_name).connect()

    media_center = server.client('420-MediaCenter')
    up = server.library.section('Movies').get('Up')
    avatar = server.library.section('Movies').get('Avatar')

    bobs = server.library.section('TV Shows').search('Bob\'s Burgers')[0]

    sorter = Sorter()
    eps = bobs.episodes()
    sorter.sort(eps)

    queue = media_center.server.createPlayQueue(eps[0])
    queue.addList(eps[1:])
    media_center.playPlayQueue(queue, eps[0])
