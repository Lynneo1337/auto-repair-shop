<template>
  <div class="login-page fade-in">
    <div class="login-container">
      <div class="login-card">
        <div class="card-header">
          <div class="logo-icon">🔧</div>
          <h1 class="card-title">ВХОД В <span class="red">СИСТЕМУ</span></h1>
          <p class="card-subtitle">Введите свои учётные данные</p>
        </div>

        <form @submit.prevent="login" class="form">
          <div class="input-group">
            <label class="label">Email или телефон</label>
            <input 
              v-model="form.login" 
              type="text" 
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
              class="input"
              placeholder="••••••••"
            />
          </div>

          <button type="submit" :disabled="loading" class="btn-submit">
            <span v-if="!loading">Войти</span>
            <span v-else>Вход...</span>
          </button>
        </form>

        <div v-if="error" class="error-message">
          <div class="error-icon">⚠️</div>
          <p>{{ error }}</p>
        </div>

        <div class="card-footer">
          <p>Нет аккаунта? <router-link to="/register" class="link">Зарегистрироваться</router-link></p>
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

const form = ref({ login: '', password: '' })
const loading = ref(false)
const error = ref(null)

const login = async () => {
  loading.value = true
  error.value = null
  
  try {
    const response = await api.post('/clients/login', {
      login: form.value.login,
      password: form.value.password
    })
    
    localStorage.setItem('access_token', response.data.access_token)
    router.push('/')
  } catch (err) {
    error.value = 'Неверный логин или пароль'
    console.error(err)
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.login-page {
  width: 100%;
  min-height: calc(100vh - 180px);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  position: relative;
  overflow: hidden;
}

.login-page::before {
  content: '';
  position: absolute;
  top: 20%;
  left: 10%;
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, rgba(220, 38, 38, 0.2) 0%, transparent 70%);
  filter: blur(80px);
  animation: glow 6s ease-in-out infinite;
}

.login-page::after {
  content: '';
  position: absolute;
  bottom: 20%;
  right: 10%;
  width: 300px;
  height: 300px;
  background: radial-gradient(circle, rgba(153, 27, 27, 0.2) 0%, transparent 70%);
  filter: blur(80px);
  animation: glow 8s ease-in-out infinite reverse;
}

.login-container {
  position: relative;
  z-index: 2;
  width: 100%;
  max-width: 450px;
}

.login-card {
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

.login-card::before {
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
  gap: 20px;
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