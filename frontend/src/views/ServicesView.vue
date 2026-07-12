<template>
  <div class="services fade-in">
    <div class="page-header">
      <h1 class="page-title">НАШИ <span class="red">УСЛУГИ</span></h1>
      <p class="page-subtitle">Полный спектр работ по ремонту и диагностике</p>
    </div>

    <div v-if="loading" class="loading">
      <div class="spinner"></div>
      <p>Загрузка услуг...</p>
    </div>

    <div v-else-if="error" class="error-card">
      <div class="error-icon">⚠️</div>
      <p>{{ error }}</p>
    </div>

    <div v-else class="services-grid">
      <div 
        v-for="service in services" 
        :key="service.id" 
        class="service-card"
      >
        <div class="service-header">
          <h3 class="service-name">{{ service.name }}</h3>
          <div class="service-price">
            <span class="price-value">{{ service.price }}</span>
            <span class="price-currency">₽</span>
          </div>
        </div>
        <div class="service-body">
          <div class="service-badge">
            <span class="badge-icon">👨‍🔧</span>
            <span>{{ service.req_specialization }}</span>
          </div>
        </div>
        <div class="service-footer">
          <button class="btn-order">Записаться</button>
        </div>
      </div>
    </div>

    <div v-if="!loading && !error && services.length === 0" class="empty-state">
      <div class="empty-icon">🛠️</div>
      <p>Услуги пока не добавлены</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '../api'

const services = ref([])
const loading = ref(true)
const error = ref(null)

onMounted(async () => {
  try {
    const response = await api.get('/services/')
    services.value = response.data
  } catch (err) {
    error.value = 'Ошибка загрузки услуг. Убедитесь, что бэкенд запущен.'
    console.error(err)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.services {
  width: 100%;
  min-height: 100vh;
  padding: 60px 40px;
  max-width: 1400px;
  margin: 0 auto;
}

.page-header {
  text-align: center;
  margin-bottom: 60px;
}

.page-title {
  font-size: clamp(2.5rem, 5vw, 4rem);
  font-weight: 900;
  color: white;
  letter-spacing: -1px;
  margin-bottom: 15px;
}

.page-title .red {
  background: linear-gradient(135deg, #ef4444, #dc2626);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  filter: drop-shadow(0 0 20px rgba(220, 38, 38, 0.5));
}

.page-subtitle {
  color: rgba(255, 255, 255, 0.7);
  font-size: 1.2rem;
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 30px;
}

.service-card {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 20px;
  overflow: hidden;
  transition: all 0.4s;
  display: flex;
  flex-direction: column;
  position: relative;
}

.service-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, #dc2626, #ef4444, #dc2626);
}

.service-card:hover {
  transform: translateY(-8px);
  border-color: rgba(220, 38, 38, 0.5);
  box-shadow: 0 20px 60px rgba(220, 38, 38, 0.3);
  background: rgba(255, 255, 255, 0.08);
}

.service-header {
  padding: 30px 25px 20px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.service-name {
  font-size: 1.3rem;
  color: white;
  margin-bottom: 15px;
  font-weight: 700;
  line-height: 1.3;
}

.service-price {
  display: flex;
  align-items: baseline;
  gap: 5px;
}

.price-value {
  font-size: 2.5rem;
  font-weight: 900;
  background: linear-gradient(135deg, #ef4444, #ffffff);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  line-height: 1;
}

.price-currency {
  font-size: 1.5rem;
  color: rgba(255, 255, 255, 0.6);
  font-weight: 700;
}

.service-body {
  padding: 20px 25px;
  flex: 1;
}

.service-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 15px;
  background: rgba(220, 38, 38, 0.15);
  border: 1px solid rgba(220, 38, 38, 0.3);
  border-radius: 20px;
  color: rgba(255, 255, 255, 0.9);
  font-size: 0.9rem;
}

.badge-icon {
  font-size: 1.1rem;
}

.service-footer {
  padding: 20px 25px 25px;
}

.btn-order {
  width: 100%;
  padding: 14px;
  background: linear-gradient(135deg, #dc2626, #991b1b);
  color: white;
  border: none;
  border-radius: 12px;
  font-weight: 700;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.btn-order:hover {
  background: linear-gradient(135deg, #ef4444, #b91c1c);
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(220, 38, 38, 0.4);
}

/* Loading */
.loading {
  text-align: center;
  padding: 80px 20px;
  color: rgba(255, 255, 255, 0.7);
}

.spinner {
  width: 50px;
  height: 50px;
  border: 3px solid rgba(220, 38, 38, 0.2);
  border-top-color: #dc2626;
  border-radius: 50%;
  margin: 0 auto 20px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Error */
.error-card {
  background: rgba(220, 38, 38, 0.1);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(220, 38, 38, 0.3);
  border-radius: 20px;
  padding: 40px;
  text-align: center;
  max-width: 500px;
  margin: 60px auto;
}

.error-icon {
  font-size: 3rem;
  margin-bottom: 15px;
}

.empty-state {
  text-align: center;
  padding: 80px 20px;
  color: rgba(255, 255, 255, 0.6);
}

.empty-icon {
  font-size: 4rem;
  margin-bottom: 20px;
  opacity: 0.5;
}
</style>