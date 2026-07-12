<template>
  <div class="home fade-in">
    <!-- Герой-секция -->
    <section class="hero">
      <div class="hero-content">
        <h1 class="hero-title">
          <span class="title-line">ПРОФЕССИОНАЛЬНЫЙ</span>
          <span class="title-line red">РЕМОНТ АВТО</span>
        </h1>
        <p class="hero-subtitle">
          Современные технологии, опытные мастера, гарантия качества
        </p>
        <div class="hero-buttons">
          <router-link to="/services" class="btn btn-outline">Наши услуги</router-link>
          <router-link to="/register" class="btn btn-primary">Записаться онлайн</router-link>
        </div>
      </div>
      <div class="hero-decoration"></div>
    </section>

    <!-- Преимущества -->
    <section class="features">
      <div class="feature-card" v-for="(feature, index) in features" :key="index">
        <div class="feature-icon">{{ feature.icon }}</div>
        <h3 class="feature-title">{{ feature.title }}</h3>
        <p class="feature-text">{{ feature.text }}</p>
      </div>
    </section>

    <!-- Статистика -->
    <section class="stats">
      <div class="stat-card">
        <div class="stat-number">5</div>
        <div class="stat-label">Мастеров</div>
      </div>
      <div class="stat-card">
        <div class="stat-number">2</div>
        <div class="stat-label">Бокса</div>
      </div>
      <div class="stat-card">
        <div class="stat-number">700+</div>
        <div class="stat-label">Довольных клиентов</div>
      </div>
      <div class="stat-card">
        <div class="stat-number">10%</div>
        <div class="stat-label">Скидка постоянным</div>
      </div>
    </section>
  </div>
</template>

<script setup>
const features = [
  {
    icon: '🔧',
    title: 'Опытные мастера',
    text: '5 специалистов различного профиля с многолетним опытом работы'
  },
  {
    icon: '🏢',
    title: '2 современных бокса',
    text: 'Оборудование последнего поколения для диагностики и ремонта'
  },
  {
    icon: '💰',
    title: 'Система скидок',
    text: 'Накопительные скидки до 10% для постоянных клиентов'
  },
  {
    icon: '⚡',
    title: 'Быстро и качественно',
    text: 'Соблюдаем сроки и гарантируем качество выполненных работ'
  }
]
</script>

<style scoped>
.home {
  width: 100%;
  min-height: 100vh;
  padding: 60px 40px;
  max-width: 1400px;
  margin: 0 auto;
}

/* Герой-секция */
.hero {
  position: relative;
  min-height: 70vh;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 80px 20px;
  overflow: hidden;
}

.hero-content {
  position: relative;
  z-index: 2;
  max-width: 900px;
}

.hero-title {
  font-size: clamp(2.5rem, 6vw, 5rem);
  font-weight: 900;
  line-height: 1.1;
  margin-bottom: 30px;
  letter-spacing: -2px;
}

.title-line {
  display: block;
  color: white;
  text-shadow: 0 0 40px rgba(255, 255, 255, 0.3);
}

.title-line.red {
  background: linear-gradient(135deg, #ef4444, #dc2626, #991b1b);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  filter: drop-shadow(0 0 30px rgba(220, 38, 38, 0.5));
}

.hero-subtitle {
  font-size: 1.3rem;
  color: rgba(255, 255, 255, 0.8);
  margin-bottom: 50px;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.hero-buttons {
  display: flex;
  gap: 20px;
  justify-content: center;
  flex-wrap: wrap;
}

.btn {
  padding: 18px 40px;
  border-radius: 12px;
  font-weight: 700;
  font-size: 1rem;
  text-decoration: none;
  transition: all 0.3s;
  display: inline-block;
  letter-spacing: 1px;
  text-transform: uppercase;
}

.btn-primary {
  background: linear-gradient(135deg, #dc2626, #991b1b);
  color: white;
  box-shadow: 0 10px 30px rgba(220, 38, 38, 0.4);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.btn-primary:hover {
  transform: translateY(-3px);
  box-shadow: 0 15px 40px rgba(220, 38, 38, 0.6);
}

.btn-outline {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  color: white;
  border: 2px solid rgba(255, 255, 255, 0.2);
}

.btn-outline:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: #dc2626;
  color: #ef4444;
  transform: translateY(-3px);
}

.hero-decoration {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(220, 38, 38, 0.3) 0%, transparent 70%);
  filter: blur(60px);
  z-index: 1;
  animation: glow 4s ease-in-out infinite;
}

/* Преимущества */
.features {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 30px;
  margin: 80px 0;
}

.feature-card {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 20px;
  padding: 40px 30px;
  text-align: center;
  transition: all 0.4s;
  position: relative;
  overflow: hidden;
}

.feature-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent, #dc2626, transparent);
  opacity: 0;
  transition: opacity 0.4s;
}

.feature-card:hover {
  transform: translateY(-10px);
  background: rgba(255, 255, 255, 0.08);
  border-color: rgba(220, 38, 38, 0.5);
  box-shadow: 0 20px 60px rgba(220, 38, 38, 0.2);
}

.feature-card:hover::before {
  opacity: 1;
}

.feature-icon {
  font-size: 3.5rem;
  margin-bottom: 20px;
  filter: drop-shadow(0 0 20px rgba(220, 38, 38, 0.5));
}

.feature-title {
  font-size: 1.4rem;
  margin-bottom: 15px;
  color: white;
  font-weight: 700;
}

.feature-text {
  color: rgba(255, 255, 255, 0.7);
  line-height: 1.6;
  font-size: 0.95rem;
}

/* Статистика */
.stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-top: 60px;
}

.stat-card {
  background: linear-gradient(135deg, rgba(220, 38, 38, 0.15), rgba(127, 29, 29, 0.1));
  backdrop-filter: blur(20px);
  border: 1px solid rgba(220, 38, 38, 0.3);
  border-radius: 20px;
  padding: 40px 20px;
  text-align: center;
  transition: all 0.3s;
}

.stat-card:hover {
  transform: scale(1.05);
  border-color: rgba(220, 38, 38, 0.6);
  box-shadow: 0 10px 40px rgba(220, 38, 38, 0.3);
}

.stat-number {
  font-size: 3.5rem;
  font-weight: 900;
  background: linear-gradient(135deg, #ef4444, #ffffff);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 10px;
  line-height: 1;
}

.stat-label {
  color: rgba(255, 255, 255, 0.8);
  font-size: 1rem;
  text-transform: uppercase;
  letter-spacing: 2px;
  font-weight: 500;
}
</style>