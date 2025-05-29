from main import main
from mangum import Mangum

handler = Mangum(main)
