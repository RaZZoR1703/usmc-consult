# USMC Consult

Одностраничный сайт консалтинговой компании USMC Consult (RU / EN / UZ).

- `src.html` — исходник страницы: стили, разметка, тексты на трёх языках, скрипты.
- `assets/` — логотип компании и логотипы клиентов.
- `build.py` — встраивает логотипы в страницу и собирает `docs/index.html` для GitHub Pages.

```bash
python3 build.py
```

Сайт публикуется через GitHub Pages из папки `docs/`.
