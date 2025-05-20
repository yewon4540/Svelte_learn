## 개념

## 사전 구성
```
npx sv create my-svelte-app
- Sckeleton minimal
- Typescript use
- none
- npm

cd my-svelte-app

npx svelte-add@latest tailwindcss

npm install

npm run dev
```

## 구조 이해
```
src
  ├─ routes : 페이지(라우트) 
  |	      .svelte 파일 생성하면 자동으로 URL 구조에 따라서 라우팅된다.
  ├─ att.html : 최상위 HTML 템플릿
  └─ lib : 공통 컴포넌트, 유틸 함수 등

static
  └─ 정적 파일 저장소

tailwind.config.ts
  └─ Tailwind 설정 파일

```
