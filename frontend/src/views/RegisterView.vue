<template>
  <div class="register-page fade-in">
    <div class="register-container">
      <div class="register-card">
        <div class="card-header">
          <div class="logo-icon">🚗</div>
          <h1 class="card-title">СОЗДАТЬ <span class="red">АККАУНТ</span></h1>
          <p class="card-subtitle">Присоединяйтесь к нашей системе</p>
        </div>

        <form @submit.prevent="register" class="form">
          <div class="input-group">
            <label class="label">ФИО</label>
            <input 
              v-model="form.full_name" 
              type="text" 
              required 
              class="input"
              placeholder="Иванов Иван Иванович"
            />
          </div>

          <div class="input-group">
            <label class="label">Телефон</label>
            <input 
              v-model="form.phone" 
              type="tel" 
              required 
              class="input"
              placeholder="+7 (999) 123-45-67"
            />
          </div>

          <div class="input-group">
            <label class="label">Email</label>
            <input 
              v-model="form.email" 
              type="email" 
              required 
              class="input"
              placeholder="example@mail.ru"
            />
          </div>

          <div class="input-group">
            <label class="label">Пароль</label>
            <input 
              v-model="form.password" 
              type="password" 
              required 
              minlength="6"
              class="input"
              placeholder="Минимум 6 символов"
            />
          </div>

          <button type="submit" :disabled="loading" class="btn-submit">
            <span v-if="!loading">Зарегистрироваться</span>
            <span v-else>Создание аккаунта...</span>
          </button>
        </form>

        <div v-if="error" class="error-message">
          <div class="error-icon">⚠️</div>
          <p>{{ error }}</p>
        </div>

        <div class="card-footer">
          <p>Уже есть аккаунт? <router-link to="/login" class="link">Войти</router-link></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '../api'

const router = useRouter()

const form = ref({
  full_name: '',
  phone: '',
  email: '',
  password: ''
})

const loading = ref(false)
const error = ref(null)

const register = async () => {
  loading.value = true
  error.value = null
  
  try {
    await api.post('/clients/', {
      full_name: form.value.full_name,
      phone: form.value.phone,
      email: form.value.email,
      password: form.value.password
    })
    
    const loginResponse = await api.post('/clients/login', {
      login: form.value.email,
      password: form.value.password
    })
    
    localStorage.setItem('access_token', loginResponse.data.access_token)
    router.push('/')
  } catch (err) {
    if (err.response?.status === 400) {
      error.value = 'Пользователь с таким email или телефоном уже существует'
    } else {
      error.value = 'Ошибка регистрации. Попробуйте позже.'
    }
    console.error(err)
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.register-page {
  width: 100%;
  min-height: calc(100vh - 180px);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  position: relative;
  overflow: hidden;
}

.register-page::before {
  content: '';
  position: absolute;
  top: 10%;
  right: 15%;
  width: 500px;
  height: 500px;
  background: radial-gradient(circle, rgba(220, 38, 38, 0.2) 0%, transparent 70%);
  filter: blur(80px);
  animation: glow 6s ease-in-out infinite;
}

.register-page::after {
  content: '';
  position: absolute;
  bottom: 10%;
  left: 10%;
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, rgba(153, 27, 27, 0.2) 0%, transparent 70%);
  filter: blur(80px);
  animation: glow 8s ease-in-out infinite reverse;
}

.register-container {
  position: relative;
  z-index: 2;
  width: 100%;
  max-width: 500px;
}

.register-card {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(30px);
  -webkit-backdrop-filter: blur(30px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 25px;
  padding: 50px 40px;
  position: relative;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
}

.register-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, #dc2626, #ef4444, #dc2626);
}

.card-header {
  text-align: center;
  margin-bottom: 35px;
}

.logo-icon {
  font-size: 3rem;
  margin-bottom: 15px;
  filter: drop-shadow(0 0 20px rgba(220, 38, 38, 0.5));
}

.card-title {
  font-size: 2rem;
  font-weight: 900;
  color: white;
  margin-bottom: 10px;
  letter-spacing: -1px;
}

.card-title .red {
  background: linear-gradient(135deg, #ef4444, #dc2626);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.card-subtitle {
  color: rgba(255, 255, 255, 0.6);
  font-size: 0.95rem;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.input-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.label {
  color: rgba(255, 255, 255, 0.8);
  font-size: 0.9rem;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.input {
  width: 100%;
  padding: 16px 20px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  color: white;
  font-size: 1rem;
  transition: all 0.3s;
  outline: none;
}

.input::placeholder {
  color: rgba(255, 255, 255, 0.3);
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

.error-message {
  margin-top: 20px;
  padding: 15px;
  background: rgba(220, 38, 38, 0.1);
  border: 1px solid rgba(220, 38, 38, 0.3);
  border-radius: 12px;
  display: flex;
  align-items: center;
  gap: 10px;
  color: #fca5a5;
  animation: fadeIn 0.4s;
}

.error-icon {
  font-size: 1.3rem;
}

.card-footer {
  margin-top: 30px;
  text-align: center;
  color: rgba(255, 255, 255, 0.6);
  font-size: 0.95rem;
}

.link {
  color: #ef4444;
  text-decoration: none;
  font-weight: 600;
  transition: color 0.3s;
}

.link:hover {
  color: #f87171;
  text-decoration: underline;
}
</style>