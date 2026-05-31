# Getting Started with GitHub Copilot

<img src="https://octodex.github.com/images/Professortocat_v2.png" align="right" height="200px" />

Hey @creator744-ui!

Mona here. I'm done preparing your exercise. Hope you enjoy! 💚

Remember, it's self-paced so feel free to take a break! ☕️

[![](https://img.shields.io/badge/Go%20to%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/creator744-ui/creator74-btc-ui/issues/1)

---

## Manual GitHub Web UI steps: GitHub Pages SPA routing fix (branch `main`)

1. Open `https://github.com/creator744-ui/creator74-btc-ui` in your browser and switch to branch **main**.
2. Edit `vite.config.ts`:
   - Open `vite.config.ts` (create it if it does not exist).
   - Click **Edit this file** (pencil icon).
   - Set Vite base to your project pages path:
     ```ts
     export default defineConfig(() => ({
       base: "/creator74-btc-ui/",
     }));
     ```
   - Click **Commit changes...** and commit directly to `main`.
3. Edit `src/App.tsx`:
   - Open `src/App.tsx` (create it if it does not exist).
   - Update `BrowserRouter` to use a basename for GitHub Pages:
     ```tsx
     <BrowserRouter basename="/creator74-btc-ui">
     ```
   - Commit the change to `main`.
4. Create `public/404.html`:
   - Go to the repository root, press **Add file** → **Create new file**.
   - Enter path: `public/404.html`.
   - Paste:
     ```html
     <!doctype html>
     <html>
       <head>
         <meta charset="utf-8" />
         <title>App</title>
         <script>
           (function () {
             var l = window.location;
             var segmentCount = 1;
             var repoBase = l.pathname.split('/').slice(0, 1 + segmentCount).join('/');
             var rest = l.pathname.slice(repoBase.length);
             var target =
               repoBase +
               '/?p=' + encodeURIComponent(rest) +
               '&q=' + encodeURIComponent(l.search.slice(1)) +
               l.hash;
             window.location.replace(target);
           })();
         </script>
       </head>
       <body></body>
     </html>
     ```
   - Commit directly to `main`.
5. Edit `src/main.tsx`:
   - Open `src/main.tsx` (create it if it does not exist).
   - Add this near the top of the file before React renders:
     ```ts
     const params = new URLSearchParams(window.location.search);
     const p = params.get("p");
     const q = params.get("q");

     if (p) {
       const newUrl =
         window.location.origin +
         "/creator74-btc-ui" +
         p +
         (q ? `?${q}` : "") +
         window.location.hash;

       window.history.replaceState(null, "", newUrl);
     }
     ```
   - Commit directly to `main`.
6. After these commits, open these URLs to verify direct-load/refresh routing works:
   - `https://creator744-ui.github.io/creator74-btc-ui/`
   - `https://creator744-ui.github.io/creator74-btc-ui/login`
   - `https://creator744-ui.github.io/creator74-btc-ui/dtx`
   - `https://creator744-ui.github.io/creator74-btc-ui/admin/login`

---

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)
