<template>
  <div class="contacts fade-in">
    <div class="page-header">
      <h1 class="page-title">КОНТАКТЫ</h1>
      <p class="page-subtitle">Свяжитесь с нами любым удобным способом</p>
    </div>

    <div class="contacts-grid">
      <!-- Инфо-блоки -->
      <div class="info-section">
        <div class="info-card" v-for="(info, index) in contactInfo" :key="index">
          <div class="info-icon">{{ info.icon }}</div>
          <h3 class="info-title">{{ info.title }}</h3>
          <p class="info-text" v-for="(line, i) in info.lines" :key="i">{{ line }}</p>
        </div>
      </div>

      <!-- Форма обратного звонка -->
      <div class="form-section">
        <div class="form-card">
          <h2 class="form-title">ЗАКАЗАТЬ <span class="red">ЗВОНОК</span></h2>
          <p class="form-subtitle">Мы перезвоним в течение 15 минут</p>

          <form @submit.prevent="submitCallback" class="form">
            <div class="input-group">
              <input 
                v-model="form.name" 
                type="text" 
                placeholder="Ваше имя" 
                required 
                class="input"
              />
            </div>
            <div class="input-group">
              <input 
                v-model="form.phone" 
                type="tel" 
                placeholder="+7 (999) 123-45-67" 
                required 
                class="input"
              />
            </div>
            <button type="submit" :disabled="submitting" class="btn-submit">
              <span v-if="!submitting">Заказать звонок</span>
              <span v-else>Отправка...</span>
            </button>
          </form>

          <div v-if="success" class="success-message">
            <div class="success-icon">✓</div>
            <p>Спасибо! Мы перезвоним вам в ближайшее время.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import api from '../api'

const contactInfo = [
  { icon: '📍', title: 'Адрес', lines: ['г. Москва', 'ул. Автомобильная, д. 15'] },
  { icon: '📱', title: 'Телефон', lines: ['+7 (999) 123-45-67'] },
  { icon: '🕐', title: 'Режим работы', lines: ['Пн-Пт: 9:00 - 20:00', 'Сб-Вс: 10:00 - 18:00'] },
  { icon: '✉️', title: 'Email', lines: ['info@autorepair.ru'] }
]

const form = ref({ name: '', phone: '' })
const submitting = ref(false)
const success = ref(false)

const submitCallback = async () => {
  submitting.value = true
  try {
    await api.post('/callback-requests/', {
      client_name: form.value.name,
      phone: form.value.phone
    })
    success.value = true
    form.value = { name: '', phone: '' }
    setTimeout(() => success.value = false, 5000)
  } catch (err) {
    alert('Ошибка отправки заявки. Попробуйте позже.')
    console.error(err)
  } finally {
    submitting.value = false
  }
}
</script>

<style scoped>
.contacts {
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
}

.page-subtitle {
  color: rgba(255, 255, 255, 0.7);
  font-size: 1.2rem;
}

.contacts-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
  align-items: start;
}

@media (max-width: 900px) {
  .contacts-grid {
    grid-template-columns: 1fr;
  }
}

.info-section {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}

.info-card {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 20px;
  padding: 30px 25px;
  transition: all 0.4s;
}

.info-card:hover {
  transform: translateY(-5px);
  border-color: rgba(220, 38, 38, 0.5);
  box-shadow: 0 15px 40px rgba(220, 38, 38, 0.2);
}

.info-icon {
  font-size: 2.5rem;
  margin-bottom: 15px;
  filter: drop-shadow(0 0 15px rgba(220, 38, 38, 0.5));
}

.info-title {
  font-size: 1.2rem;
  color: white;
  margin-bottom: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.info-text {
  color: rgba(255, 255, 255, 0.7);
  line-height: 1.6;
  font-size: 0.95rem;
}

.form-section {
  position: sticky;
  top: 100px;
}

.form-card {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(220, 38, 38, 0.3);
  border-radius: 25px;
  padding: 50px 40px;
  position: relative;
  overflow: hidden;
}

.form-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, #dc2626, #ef4444, #dc2626);
}

.form-title {
  font-size: 2rem;
  font-weight: 900;
  color: white;
  margin-bottom: 10px;
  letter-spacing: -1px;
}

.form-title .red {
  background: linear-gradient(135deg, #ef4444, #dc2626);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.form-subtitle {
  color: rgba(255, 255, 255, 0.6);
  margin-bottom: 30px;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.input-group {
  position: relative;
}

.input {
  width: 100%;
  padding: 18px 20px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  color: white;
  font-size: 1rem;
  transition: all 0.3s;
  outline: none;
}

.input::placeholder {
  color: rgba(255, 255, 255, 0.4);
}

.input:focus {
  background: rgba(255, 255, 255, 0.08);
  border-color: #dc2626;
  box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.2);
}

.btn-submit {
  padding: 18px;
  background: linear-gradient(135deg, #dc2626, #991b1b);
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.3s;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-top: 10px;
}

.btn-submit:hover:not(:disabled) {
  background: linear-gradient(135deg, #ef4444, #b91c1c);
  transform: translateY(-2px);
  box-shadow: 0 10px 30px rgba(220, 38, 38, 0.5);
}

.btn-submit:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.success-message {
  margin-top: 25px;
  padding: 20px;
  background: rgba(34, 197, 94, 0.1);
  border: 1px solid rgba(34, 197, 94, 0.3);
  border-radius: 12px;
  text-align: center;
  animation: fadeIn 0.4s;
}

.success-icon {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, #22c55e, #16a34a);
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  font-weight: bold;
  margin: 0 auto 10px;
}

.success-message p {
  color: rgba(255, 255, 255, 0.9);
}
</style>