from http_fw.router import Router
from http_fw.server import run
from app.ads import AdsController
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

config = {
    'host': 'localhost',
    'port': 9000,
    'static':os.path.join(BASE_DIR, 'static')
}

router = Router()

router.get('/',AdsController,'index')
router.get('/ads',AdsController,'index')
router.get('/ads/new',AdsController,'new')
router.post('/ads',AdsController,'create')
router.get('/ad',AdsController,'ad')
run(router,config)