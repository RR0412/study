from http_fw.router import Router
from http_fw.server import run

from app.post import PostController

config = {
    'host': 'localhost',
    'port': 8000,
    'static': 'static'
}

router = Router()

router.get('/', PostController, 'index')
router.get('/posts', PostController, 'index')
router.get('/posts/new', PostController, 'new')
router.get('/post',PostController,'view_post')
router.post('/posts', PostController, 'create')

run(router, config)
