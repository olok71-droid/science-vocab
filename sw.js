// AMY Study App — Service Worker
// 빌드 버전: v20260525-010354
// 새 버전이 push되면 자동으로 클라이언트 새로고침.

const CACHE_VERSION = 'v20260525-010354';
const CACHE_NAME = 'amy-study-' + CACHE_VERSION;
const CORE_FILES = ["./", "biology.html", "chemistry.html", "ecosystems.html", "atoms.html", "forces.html", "atmosphere.html", "motion.html", "pressure.html", "purity.html", "eal.html", "history.html", "geo_population.html", "geo_migration.html", "index.html"];

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME).then(function(cache) {
      // 핵심 파일 미리 캐시 (실패해도 진행)
      return Promise.allSettled(CORE_FILES.map(function(url) {
        return cache.add(url).catch(function() {});
      }));
    })
  );
});

self.addEventListener('activate', function(event) {
  event.waitUntil(
    caches.keys().then(function(keys) {
      return Promise.all(keys.map(function(key) {
        if (key !== CACHE_NAME) return caches.delete(key);
      }));
    }).then(function() {
      return self.clients.claim(); // 즉시 모든 페이지 통제
    })
  );
});

// 메시지로 즉시 활성화 명령 받기
self.addEventListener('message', function(event) {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});

// Network-first 전략 (항상 새 버전 우선, 실패 시 캐시)
self.addEventListener('fetch', function(event) {
  if (event.request.method !== 'GET') return;
  var url = new URL(event.request.url);
  // 다른 도메인은 패스 (Anthropic API, YouTube 등)
  if (url.origin !== self.location.origin) return;
  event.respondWith(
    fetch(event.request).then(function(resp) {
      // 성공 → 캐시 업데이트 + 응답
      var clone = resp.clone();
      caches.open(CACHE_NAME).then(function(cache) {
        cache.put(event.request, clone).catch(function() {});
      });
      return resp;
    }).catch(function() {
      // 오프라인 → 캐시에서
      return caches.match(event.request);
    })
  );
});
