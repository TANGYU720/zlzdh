<template>
  <div class="contact">
    <section class="page-header">
      <div class="container">
        <h1>联系我们</h1>
        <p>欢迎联系我们，我们将竭诚为您服务</p>
      </div>
    </section>

    <section class="contact-content">
      <div class="container">
        <div class="contact-info">
          <div class="info-card">
            <div class="info-icon">📍</div>
            <div class="info-content">
              <h3>公司地址</h3>
              <p>上海市浦东新区张江高科技园区</p>
              <p>工业自动化大厦18层</p>
            </div>
          </div>
          <div class="info-card">
            <div class="info-icon">📞</div>
            <div class="info-content">
              <h3>联系电话</h3>
              <p>400-888-8888（全国服务热线）</p>
              <p>021-5888-8888（上海总部）</p>
            </div>
          </div>
          <div class="info-card">
            <div class="info-icon">✉️</div>
            <div class="info-content">
              <h3>电子邮箱</h3>
              <p>contact@zhilian-auto.com</p>
              <p>sales@zhilian-auto.com（商务合作）</p>
            </div>
          </div>
          <div class="info-card">
            <div class="info-icon">🕐</div>
            <div class="info-content">
              <h3>工作时间</h3>
              <p>周一至周五：09:00 - 18:00</p>
              <p>周六：09:00 - 12:00</p>
            </div>
          </div>
        </div>

        <div class="contact-form-section">
          <h2>发送消息</h2>
          <form class="contact-form" @submit.prevent="submitForm">
            <div class="form-row">
              <div class="form-group">
                <label>姓名 *</label>
                <input type="text" v-model="form.name" placeholder="请输入您的姓名" required />
              </div>
              <div class="form-group">
                <label>电话 *</label>
                <input type="tel" v-model="form.phone" placeholder="请输入您的联系电话" required />
              </div>
            </div>
            <div class="form-row">
              <div class="form-group">
                <label>邮箱</label>
                <input type="email" v-model="form.email" placeholder="请输入您的邮箱" />
              </div>
              <div class="form-group">
                <label>公司名称</label>
                <input type="text" v-model="form.company" placeholder="请输入您的公司名称" />
              </div>
            </div>
            <div class="form-group">
              <label>咨询类型</label>
              <select v-model="form.type">
                <option value="product">产品咨询</option>
                <option value="project">项目合作</option>
                <option value="service">技术服务</option>
                <option value="other">其他</option>
              </select>
            </div>
            <div class="form-group">
              <label>留言内容 *</label>
              <textarea v-model="form.message" placeholder="请输入您的留言内容..." rows="5" required></textarea>
            </div>
            <div class="form-group checkbox-group">
              <input type="checkbox" v-model="form.agreement" id="agreement" />
              <label for="agreement">我已阅读并同意<a href="#">《隐私政策》</a>和<a href="#">《服务条款》</a></label>
            </div>
            <button type="submit" class="submit-btn" :disabled="!form.agreement">
              <span>📤</span>
              <span>发送消息</span>
            </button>
          </form>

          <div class="success-message" v-if="showSuccess">
            <span class="success-icon">✅</span>
            <h3>消息发送成功！</h3>
            <p>我们会在24小时内与您联系</p>
          </div>

          <div class="error-message" v-if="showError">
            <span class="error-icon">❌</span>
            <h3>提交失败</h3>
            <p>{{ errorMessage }}</p>
          </div>
        </div>
      </div>
    </section>

    <section class="map-section">
      <div class="container">
        <h2>公司位置</h2>
        <div class="map-placeholder">
          <div class="map-content">
            <div class="map-icon">🗺️</div>
            <p>上海市浦东新区张江高科技园区</p>
            <p>工业自动化大厦18层</p>
            <div class="map-links">
              <button class="map-btn">🚌 公交路线</button>
              <button class="map-btn">🚇 地铁线路</button>
              <button class="map-btn">🚗 驾车导航</button>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'

const form = reactive({
  name: '',
  phone: '',
  email: '',
  company: '',
  type: 'product',
  message: '',
  agreement: false
})

const showSuccess = ref(false)
const showError = ref(false)
const errorMessage = ref('')
const isSubmitting = ref(false)

const submitForm = async () => {
  if (!form.agreement) return
  if (isSubmitting.value) return
  
  isSubmitting.value = true
  showError.value = false
  
  try {
    const response = await fetch('http://localhost:8000/api/submit-contact/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        name: form.name,
        phone: form.phone,
        email: form.email,
        company: form.company,
        inquiry_type: form.type,
        message: form.message
      })
    })
    
    const data = await response.json()
    
    if (data.success) {
      showSuccess.value = true
      form.name = ''
      form.phone = ''
      form.email = ''
      form.company = ''
      form.type = 'product'
      form.message = ''
      form.agreement = false
      
      setTimeout(() => {
        showSuccess.value = false
      }, 3000)
    } else {
      showError.value = true
      errorMessage.value = data.message || '提交失败'
      setTimeout(() => {
        showError.value = false
      }, 5000)
    }
  } catch (error) {
    showError.value = true
    errorMessage.value = '网络错误，请稍后重试'
    setTimeout(() => {
      showError.value = false
    }, 5000)
  } finally {
    isSubmitting.value = false
  }
}
</script>

<style scoped>
.page-header {
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
  color: white;
  padding: 40px 0;
  text-align: center;
}

.page-header h1 {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
}

.page-header p {
  color: #94a3b8;
}

.contact-content {
  padding: 40px 0;
}

.contact-content .container {
  display: grid;
  grid-template-columns: 400px 1fr;
  gap: 3rem;
}

.contact-info {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.info-card {
  display: flex;
  gap: 1rem;
  background: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

.info-icon {
  font-size: 2rem;
}

.info-content h3 {
  color: #0f172a;
  margin-bottom: 0.3rem;
}

.info-content p {
  color: #64748b;
  font-size: 0.9rem;
  margin: 0.2rem 0;
}

.contact-form-section {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

.contact-form-section h2 {
  color: #0f172a;
  margin-bottom: 1.5rem;
}

.contact-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-group label {
  font-weight: 500;
  color: #0f172a;
  margin-bottom: 0.3rem;
}

.form-group input,
.form-group select,
.form-group textarea {
  padding: 0.8rem;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  font-size: 1rem;
  transition: border-color 0.3s;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #06b6d4;
}

.checkbox-group {
  flex-direction: row;
  align-items: center;
  gap: 0.5rem;
}

.checkbox-group input {
  width: auto;
}

.checkbox-group label {
  font-weight: normal;
  color: #64748b;
  font-size: 0.9rem;
}

.checkbox-group a {
  color: #06b6d4;
  text-decoration: none;
}

.submit-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 1rem;
  background: linear-gradient(135deg, #06b6d4, #3b82f6);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s;
}

.submit-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 5px 20px rgba(6, 182, 212, 0.3);
}

.submit-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.success-message {
  text-align: center;
  padding: 2rem;
  background: #dcfce7;
  border-radius: 8px;
  margin-top: 1rem;
}

.success-icon {
  font-size: 3rem;
  display: block;
  margin-bottom: 0.5rem;
}

.success-message h3 {
  color: #16a34a;
  margin-bottom: 0.3rem;
}

.success-message p {
  color: #64748b;
}

.error-message {
  text-align: center;
  padding: 2rem;
  background: #fee2e2;
  border-radius: 8px;
  margin-top: 1rem;
}

.error-icon {
  font-size: 3rem;
  display: block;
  margin-bottom: 0.5rem;
}

.error-message h3 {
  color: #dc2626;
  margin-bottom: 0.3rem;
}

.error-message p {
  color: #64748b;
}

.map-section {
  padding: 40px 0;
  margin-top: 2rem;
}

.map-section h2 {
  text-align: center;
  color: #0f172a;
  margin-bottom: 1.5rem;
}

.map-placeholder {
  background: linear-gradient(135deg, #0f172a, #1e293b);
  border-radius: 12px;
  padding: 4rem;
}

.map-content {
  text-align: center;
  color: white;
}

.map-icon {
  font-size: 4rem;
  margin-bottom: 1rem;
}

.map-content p {
  color: #94a3b8;
  margin: 0.3rem 0;
}

.map-links {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-top: 1.5rem;
}

.map-btn {
  padding: 0.8rem 1.5rem;
  background: rgba(6, 182, 212, 0.2);
  border: 1px solid #06b6d4;
  color: #06b6d4;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.3s;
}

.map-btn:hover {
  background: #06b6d4;
  color: white;
}

@media (max-width: 768px) {
  .contact-content .container {
    grid-template-columns: 1fr;
  }
  
  .form-row {
    grid-template-columns: 1fr;
  }
  
  .checkbox-group {
    flex-wrap: wrap;
  }
  
  .map-links {
    flex-direction: column;
  }
}
</style>
