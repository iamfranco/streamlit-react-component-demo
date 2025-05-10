# My Component

Install npm packages:
```
npm i
```

### Running locally (hot reload)
Run React component locally:
```
npm run start
```

The component will be running at http://localhost:3001
It will appear blank, this is normal

Open another terminal, cd to the base of the repo (where `app.py` resides), and run the streamlit app
```
streamlit run __init__.py --server.port=8510
```

Then you should see the streamlit app rendering the react component.

---

### Release

When happy with the react component, then build it
```
npm run build
```

This builds it into the `build/` folder.
