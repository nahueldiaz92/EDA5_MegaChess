import asyncio
import json
from random import randint
import sys
import websockets
import board_moves

AUTH_TOKEN = '24f4a9db-f299-4508-933a-30eb96dadac1'
async def send(websocket, action, data):
    message = json.dumps(
        {
            'action': action,
            'data': data,
        }
    )
    await websocket.send(message)


async def start():
    uri = "ws://megachess.herokuapp.com/service?authtoken={}".format(AUTH_TOKEN)
    async with websockets.connect(uri) as websocket:
        while True:
            try:
                response = await websocket.recv()
                data = json.loads(response)
                
                if data['event'] == 'update_user_list':
                    print(data["data"]["users_list"])
                    pass
                if data['event'] == 'gameover':
                    print(data)
                    pass
                if data['event'] == 'ask_challenge':
                    pass
                """
                    await send(
                        websocket,
                        'accept_challenge',
                        {
                            'board_id': data['data']['board_id'],
                        },
                    )
                    """
                if data['event'] == 'your_turn':
                    if data["data"]["actual_turn"] == "white": 
                        print("Blanca")  
                        board = board_moves.get_board(data["data"]["board"])
                        x = board_moves.moving_white(board)
                        await send(
                            websocket,
                            'move', {
                                'board_id': data['data']['board_id'],
                                'turn_token': data['data']['turn_token'],
                                'from_row': x[0][0],
                                'from_col': x[0][1],
                                'to_row': x[0][2],
                                'to_col': x[0][3]}                   
                            )
                    else:
                        print("Negra")
                        board = board_moves.get_board(data["data"]["board"])
                        y = board_moves.moving_black(board)
                        await send(
                            websocket,
                            'move', {
                                'board_id': data['data']['board_id'],
                                'turn_token': data['data']['turn_token'],
                                'from_row': int(y[0][0]),
                                'from_col': int(y[0][1]),
                                'to_row': int(y[0][2]),
                                'to_col': int(y[0][3])}      
                        )
            except Exception as e:
                print(e)
                print("retry")



if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(start())