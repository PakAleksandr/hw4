from aiogram.utils import executor
from config import dp
from hendlers import fsm_admin, fsm_client
import logging



fsm_admin.register_handlers_fsmadmin(dp)
fsm_client.register_handlers_fsmclient(dp)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)