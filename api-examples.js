// API Integration Examples
// Примеры интеграции с бэкендом

// ======================
// 1. ОТПРАВКА ФОРМЫ ОБРАТНОЙ СВЯЗИ
// ======================

/**
 * Отправка формы на сервер
 */
async function submitContactForm(formData) {
    const endpoint = 'https://your-api.com/api/contact';
    
    try {
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        return { success: true, data };
    } catch (error) {
        console.error('Error submitting form:', error);
        return { success: false, error: error.message };
    }
}

// ======================
// 2. ПОЛУЧЕНИЕ СПИСКА КУРСОВ
// ======================

/**
 * Загрузка курсов с сервера
 */
async function fetchCourses(filters = {}) {
    const endpoint = 'https://your-api.com/api/courses';
    const params = new URLSearchParams(filters);
    
    try {
        const response = await fetch(`${endpoint}?${params}`);
        const courses = await response.json();
        
        return courses;
    } catch (error) {
        console.error('Error fetching courses:', error);
        return [];
    }
}

/**
 * Отображение курсов на странице
 */
function renderCourses(courses) {
    const container = document.querySelector('.courses-grid');
    
    courses.forEach(course => {
        const card = createCourseCard(course);
        container.appendChild(card);
    });
}

function createCourseCard(course) {
    const card = document.createElement('div');
    card.className = 'course-card';
    card.innerHTML = `
        <div class="course-image">
            <div class="course-category">${course.category}</div>
            <div class="course-thumbnail" style="background-image: url('${course.image}');"></div>
        </div>
        <div class="course-content">
            <h3>${course.title}</h3>
            <p>${course.description}</p>
            <div class="course-meta">
                <span class="course-duration">⏱ ${course.duration}</span>
                <span class="course-students">👥 ${course.students} студентов</span>
            </div>
            <div class="course-footer">
                <div class="course-price">
                    ${course.oldPrice ? `<span class="price-old">${course.oldPrice}₽</span>` : ''}
                    <span class="price-new">${course.price}₽</span>
                </div>
                <a href="/course/${course.id}" class="btn-primary">Записаться</a>
            </div>
        </div>
    `;
    return card;
}

// ======================
// 3. РЕГИСТРАЦИЯ ПОЛЬЗОВАТЕЛЯ
// ======================

/**
 * Регистрация нового пользователя
 */
async function registerUser(userData) {
    const endpoint = 'https://your-api.com/api/register';
    
    try {
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: userData.name,
                email: userData.email,
                password: userData.password
            })
        });

        const data = await response.json();
        
        if (data.token) {
            // Сохранение токена
            localStorage.setItem('authToken', data.token);
            localStorage.setItem('user', JSON.stringify(data.user));
            return { success: true, user: data.user };
        }
        
        return { success: false, error: data.message };
    } catch (error) {
        return { success: false, error: error.message };
    }
}

// ======================
// 4. АУТЕНТИФИКАЦИЯ
// ======================

/**
 * Вход пользователя
 */
async function loginUser(email, password) {
    const endpoint = 'https://your-api.com/api/login';
    
    try {
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });

        const data = await response.json();
        
        if (data.token) {
            localStorage.setItem('authToken', data.token);
            localStorage.setItem('user', JSON.stringify(data.user));
            return { success: true, user: data.user };
        }
        
        return { success: false, error: data.message };
    } catch (error) {
        return { success: false, error: error.message };
    }
}

/**
 * Выход пользователя
 */
function logoutUser() {
    localStorage.removeItem('authToken');
    localStorage.removeItem('user');
    window.location.href = '/';
}

/**
 * Проверка авторизации
 */
function isAuthenticated() {
    return !!localStorage.getItem('authToken');
}

/**
 * Получение текущего пользователя
 */
function getCurrentUser() {
    const userStr = localStorage.getItem('user');
    return userStr ? JSON.parse(userStr) : null;
}

// ======================
// 5. ЗАЩИЩЕННЫЕ ЗАПРОСЫ
// ======================

/**
 * Fetch с авторизацией
 */
async function authenticatedFetch(url, options = {}) {
    const token = localStorage.getItem('authToken');
    
    if (!token) {
        throw new Error('Not authenticated');
    }
    
    const headers = {
        ...options.headers,
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
    };
    
    return fetch(url, { ...options, headers });
}

/**
 * Запись на курс
 */
async function enrollCourse(courseId) {
    const endpoint = `https://your-api.com/api/courses/${courseId}/enroll`;
    
    try {
        const response = await authenticatedFetch(endpoint, {
            method: 'POST'
        });
        
        const data = await response.json();
        return { success: true, data };
    } catch (error) {
        return { success: false, error: error.message };
    }
}

// ======================
// 6. ПОДПИСКА НА РАССЫЛКУ
// ======================

/**
 * Подписка на новости
 */
async function subscribeToNewsletter(email) {
    const endpoint = 'https://your-api.com/api/newsletter/subscribe';
    
    try {
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email })
        });

        const data = await response.json();
        return { success: response.ok, message: data.message };
    } catch (error) {
        return { success: false, error: error.message };
    }
}

// ======================
// 7. ПОЛУЧЕНИЕ СТАТИСТИКИ
// ======================

/**
 * Загрузка статистики платформы
 */
async function fetchPlatformStats() {
    const endpoint = 'https://your-api.com/api/stats';
    
    try {
        const response = await fetch(endpoint);
        const stats = await response.json();
        
        // Обновление счетчиков на странице
        updateStatsOnPage(stats);
        
        return stats;
    } catch (error) {
        console.error('Error fetching stats:', error);
        return null;
    }
}

function updateStatsOnPage(stats) {
    const statElements = {
        students: document.querySelector('.stat-number[data-stat="students"]'),
        courses: document.querySelector('.stat-number[data-stat="courses"]'),
        satisfaction: document.querySelector('.stat-number[data-stat="satisfaction"]')
    };
    
    if (statElements.students) {
        animateCounter(statElements.students, stats.students);
    }
    if (statElements.courses) {
        animateCounter(statElements.courses, stats.courses);
    }
    if (statElements.satisfaction) {
        animateCounter(statElements.satisfaction, stats.satisfaction);
    }
}

// ======================
// 8. ОБРАБОТКА ПЛАТЕЖЕЙ
// ======================

/**
 * Создание платежа
 */
async function createPayment(planId) {
    const endpoint = 'https://your-api.com/api/payments/create';
    
    try {
        const response = await authenticatedFetch(endpoint, {
            method: 'POST',
            body: JSON.stringify({ planId })
        });
        
        const data = await response.json();
        
        if (data.paymentUrl) {
            // Перенаправление на страницу оплаты
            window.location.href = data.paymentUrl;
        }
        
        return { success: true, data };
    } catch (error) {
        return { success: false, error: error.message };
    }
}

// ======================
// 9. ПОИСК КУРСОВ
// ======================

/**
 * Поиск курсов
 */
async function searchCourses(query, filters = {}) {
    const endpoint = 'https://your-api.com/api/courses/search';
    const params = new URLSearchParams({
        q: query,
        ...filters
    });
    
    try {
        const response = await fetch(`${endpoint}?${params}`);
        const results = await response.json();
        
        return results;
    } catch (error) {
        console.error('Error searching courses:', error);
        return [];
    }
}

// ======================
// 10. ОТЗЫВЫ
// ======================

/**
 * Отправка отзыва
 */
async function submitReview(courseId, review) {
    const endpoint = `https://your-api.com/api/courses/${courseId}/reviews`;
    
    try {
        const response = await authenticatedFetch(endpoint, {
            method: 'POST',
            body: JSON.stringify({
                rating: review.rating,
                comment: review.comment
            })
        });
        
        const data = await response.json();
        return { success: true, data };
    } catch (error) {
        return { success: false, error: error.message };
    }
}

/**
 * Получение отзывов
 */
async function fetchReviews(courseId, page = 1) {
    const endpoint = `https://your-api.com/api/courses/${courseId}/reviews?page=${page}`;
    
    try {
        const response = await fetch(endpoint);
        const reviews = await response.json();
        
        return reviews;
    } catch (error) {
        console.error('Error fetching reviews:', error);
        return [];
    }
}

// ======================
// ЭКСПОРТ (для использования в других файлах)
// ======================

export {
    submitContactForm,
    fetchCourses,
    renderCourses,
    registerUser,
    loginUser,
    logoutUser,
    isAuthenticated,
    getCurrentUser,
    enrollCourse,
    subscribeToNewsletter,
    fetchPlatformStats,
    createPayment,
    searchCourses,
    submitReview,
    fetchReviews
};
