import uvicorn
import sys

if __name__ == '__main__':
    sys.argv.insert(1, "app.main:app")
    sys.exit(uvicorn.main())