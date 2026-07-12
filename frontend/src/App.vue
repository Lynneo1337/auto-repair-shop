<template>
  <div id="app">
    <!-- Навигация -->
    <nav class="navbar">
      <div class="nav-container">
        <router-link to="/" class="logo">
          <span class="logo-icon">🔧</span>
          <span class="logo-text">AUTO<span class="red">REPAIR</span></span>
        </router-link>
        
        <ul class="nav-links">
          <li><router-link to="/" class="nav-link">Главная</router-link></li>
          <li><router-link to="/services" class="nav-link">Услуги</router-link></li>
          <li><router-link to="/contacts" class="nav-link">Контакты</router-link></li>
          <li v-if="!isLoggedIn">
            <router-link to="/login" class="nav-link btn-login">Вход</router-link>
          </li>
          <li v-if="!isLoggedIn">
            <router-link to="/register" class="nav-link btn-register">Регистрация</router-link>
          </li>
          <li v-if="isLoggedIn">
            <button @click="logout" class="nav-link btn-logout">Выход</button>
          </li>
        </ul>
      </div>
    </nav>

    <!-- Основной контент -->
    <main class="main-content">
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>

    <!-- Подвал -->
    <footer class="glass-footer">
      <div class="footer-container">
        
        <!-- Левая колонка: Контакты -->
        <div class="footer-col contacts">
          <p class="phone">+7 (999) 123-45-67</p>
          <p class="address">г. Москва, г. Москва, ул. Автомобильная, д. 15</p>
        </div>

        <!-- Центральная колонка: Соцсети и Email -->
        <div class="footer-col center">
          <div class="socials">
            <!-- VK Icon -->
            <a href="#" class="social-link">
              <svg viewBox="0 0 24 24" fill="currentColor"><path d="M15.07 2H8.93C3.33 2 2 3.33 2 8.93v6.14C2 20.67 3.33 22 8.93 22h6.14c5.6 0 6.93-1.33 6.93-6.93V8.93C22 3.33 20.67 2 15.07 2zm3.39 13.85c-.17.26-.62.63-1.3.77-.24.05-.72-.02-1.49-.77-.35-.34-.6-.86-.88-1.35-.33-.58-.7-1.08-1.13-1.08-.39 0-.55.32-.55.76v1.13c0 .26-.22.51-.53.51-.25 0-.83-.13-2.09-.73-2.59-1.25-4.22-4.52-4.22-4.52-.15-.33-.01-.61.32-.61h1.92c.26 0 .47.12.58.37.58 1.43 1.37 2.74 1.78 2.74.14 0 .2-.06.2-.4V9.4c0-.28.25-.47.58-.47.47 0 .8.22.8 1.13v2.25c0 .26.23.51.53.51.25 0 .48-.13.87-.53 1.18-1.21 2.03-3.16 2.03-3.16.11-.23.36-.4.67-.4h1.92c.29 0 .44.15.36.43-.14.38-1.28 2.75-1.34 2.89-.17.38-.22.53 0 .91.21.36.87 1.15 1.32 1.74.6.79.6.98-.03 1.59z"/></svg>
            </a>
            <!-- OK Icon -->
            <a href="#" class="social-link">
              <svg viewBox="0 0 24 24" fill="currentColor"><path d="M14.08 10.8c-.96 1.02-2.3 1.6-3.77 1.6-1.47 0-2.81-.58-3.77-1.6-2.37-2.5-2.37-6.57 0-9.07C8.93.27 12.97.27 15.36 1.73c1.23 1.27 1.96 2.95 2.04 4.77h-1.94c-.08-1.41-.64-2.71-1.57-3.67C12.14 1.05 8.6 1.05 6.85 2.83c-1.6 1.65-1.6 4.33 0 5.98 1.75 1.78 5.29 1.78 7.04 0 .93-.96 1.49-2.26 1.57-3.67h1.94c-.08 1.82-.81 3.5-2.04 4.77-.26.27-.52.5-.78.69zm-1.82 3.37c.96 0 1.73.77 1.73 1.73 0 .96-.77 1.73-1.73 1.73-.96 0-1.73-.77-1.73-1.73 0-.96.77-1.73 1.73-1.73zm-4.52 0c.96 0 1.73.77 1.73 1.73 0 .96-.77 1.73-1.73 1.73-.96 0-1.73-.77-1.73-1.73 0-.96.77-1.73 1.73-1.73z"/></svg>
            </a>
          </div>
          <p class="email">mail@company.ru</p>
        </div>

        <!-- Правая колонка: Юр. информация -->
        <div class="footer-col legal">
          <p class="legal-info">ИНН 0000000000</p>
          <p class="legal-info">ОГРН 0000000000</p>
          <p class="copyright">Copyright © 2025 - 2026</p>
        </div>

      </div>
    </footer>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const isLoggedIn = computed(() => {
  return !!localStorage.getItem('access_token')
})

const logout = () => {
  localStorage.removeItem('access_token')
  router.push('/')
}
</script>

<style scoped>
.navbar {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(10, 10, 10, 0.7);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(220, 38, 38, 0.3);
  box-shadow: 0 4px 30px rgba(220, 38, 38, 0.1);
}

.nav-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 20px 40px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
  color: white;
  transition: transform 0.3s;
}

.logo:hover {
  transform: scale(1.05);
}

.logo-icon {
  font-size: 2rem;
  filter: drop-shadow(0 0 10px rgba(220, 38, 38, 0.5));
}

.logo-text {
  font-size: 1.5rem;
  font-weight: 900;
  letter-spacing: 2px;
  color: white;
}

.logo-text .red {
  color: #dc2626;
  text-shadow: 0 0 20px rgba(220, 38, 38, 0.5);
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 10px;
  align-items: center;
}

.nav-link {
  color: white;
  text-decoration: none;
  padding: 10px 20px;
  border-radius: 10px;
  font-weight: 500;
  transition: all 0.3s;
  position: relative;
  background: transparent;
  border: none;
  cursor: pointer;
  font-size: 1rem;
}

.nav-link:hover {
  background: rgba(220, 38, 38, 0.2);
  color: #ef4444;
}

.nav-link.router-link-active {
  background: rgba(220, 38, 38, 0.3);
  color: #ef4444;
}

.btn-login {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.btn-login:hover {
  background: rgba(255, 255, 255, 0.2);
}

.btn-register {
  background: linear-gradient(135deg, #dc2626, #991b1b);
  box-shadow: 0 4px 15px rgba(220, 38, 38, 0.4);
}

.btn-register:hover {
  background: linear-gradient(135deg, #ef4444, #b91c1c);
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(220, 38, 38, 0.6);
  color: white;
}

.btn-logout {
  background: rgba(220, 38, 38, 0.2);
  border: 1px solid rgba(220, 38, 38, 0.4);
}

.btn-logout:hover {
  background: rgba(220, 38, 38, 0.4);
  color: white;
}

.main-content {
  flex: 1;
  width: 100%;
  min-height: calc(100vh - 180px);
}

/* Анимация переходов между страницами */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.fade-enter-from {
  opacity: 0;
  transform: translateY(10px);
}

.fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

/* Обязательно: прижимаем футер к низу */
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  width: 100%;
}

.main-content {
  flex: 1; /* Растягивает контент, толкая футер вниз */
  width: 100%;
}

/* --- Стили нового футера --- */

.glass-footer {
  width: 100%;
  background: rgba(10, 10, 10, 0.6); /* Полупрозрачный черный */
  backdrop-filter: blur(15px);        /* Эффект размытия стекла */
  -webkit-backdrop-filter: blur(15px); /* Для Safari */
  border-top: 1px solid rgba(255, 255, 255, 0.08); /* Тонкая рамка сверху */
  padding: 40px 20px;
  margin-top: auto;
  color: #ffffff;
}

.footer-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 40px;
  flex-wrap: wrap;
}

.footer-col {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

/* Центрируем среднюю колонку */
.footer-col.center {
  align-items: center;
}

/* Левая колонка */
.phone {
  font-size: 1.2rem;
  font-weight: 700;
  letter-spacing: 0.5px;
}

.address {
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.95rem;
}

/* Соцсети */
.socials {
  display: flex;
  gap: 15px;
  margin-bottom: 5px;
}

.social-link {
  width: 40px;
  height: 40px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  transition: all 0.3s;
}

.social-link svg {
  width: 24px;
  height: 24px;
}

.social-link:hover {
  background: #dc2626; /* Красный при наведении */
  transform: translateY(-3px);
  box-shadow: 0 5px 15px rgba(220, 38, 38, 0.4);
}

.email {
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.95rem;
}

/* Юр. информация */
.legal-info {
  color: rgba(255, 255, 255, 0.5);
  font-size: 0.85rem;
  font-family: monospace; /* Шрифт как в документах */
}

.copyright {
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.9rem;
  margin-top: 5px;
}

/* Адаптивность для мобильных */
@media (max-width: 768px) {
  .footer-container {
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 30px;
  }
}
</style>