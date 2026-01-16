<!-- 詳細職缺列表 -->

<script setup>
import { useRoute } from 'vue-router';
import { ref, onMounted } from 'vue';
import axios from 'axios';

const route = useRoute()
const jobID = route.params.id

const job = ref(null)
const loading = ref(true)
const error = ref(null)

// Axios call API 取得jobs detail
const fetchJobDetail = async () => {
    try {
        const res = await axios.get(`http://127.0.0.1:8000/jobs/${jobID}`)
        job.value = res.data
    } catch (e) {
        error.value = `無法取得資料:+ ${e.message}`
    } finally {
        loading.value = false
    }
}

onMounted(() => {
    fetchJobDetail()
})
</script>

<template>
    <div class="min-h-screen bg-stone-100 py-10">
        <div class="max-w-4xl mx-auto px-6">
            <div v-if="loading" class="text-center text-stone-500">
                載入中...
            </div>
            <div v-else-if="error" class="text-red-600 text-center">
                {{ error }}
            </div>
            <div v-else-if="job">
                <h1 class="text-3xl text-center font-bold text-stone-800 mb-6">
                    {{ job.name }}
                </h1>
                <div class="bg-white rounded-xl shadow-sm p-8 space-y-6">
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
                        <div>
                            <p class="text-sm text-stone-500">公司</p>
                            <p class="text-lg font-medium text-stone-800">
                                {{ job.company }}
                            </p>
                        </div>
                        <div>
                            <p class="text-sm text-stone-500">地區</p>
                            <p class="text-lg font-medium text-stone-800">
                                {{ job.addr }}
                            </p>
                        </div>
                        <div>
                            <p class="text-sm text-stone-500">薪資</p>
                            <p class="text-lg font-semibold text-emerald-600">
                                {{ job.salary }}
                            </p>
                        </div>
                        <div>
                            <p class="text-sm text-stone-500">上班時間</p>
                            <p class="text-lg font-medium text-stone-800">
                                {{ job.workingtime }}
                            </p>
                        </div>
                    </div>

                    <hr class="border-stone-200" />

                    <div class="space-y-5">
                        <div>
                            <p class="text-sm text-stone-500 mb-1">完整地址</p>
                            <p class="text-stone-800">
                                {{ job.realAddr }}
                            </p>
                        </div>

                        <div>
                            <p class="text-sm text-stone-500 mb-1">所需技能</p>
                            <p class="text-stone-800">
                                {{ job.skill }}
                            </p>
                        </div>

                        <div>
                            <p class="text-sm text-stone-500 mb-1">工作內容</p>
                            <p class="text-stone-800 leading-relaxed whitespace-pre-wrap">
                                {{ job.description }}
                            </p>
                        </div>
                    </div>
                    <div class="pt-4">
                        <a :href="job.link" target="_blank" class="
                            flex
                            items-center
                            justify-center
                            bg-stone-800
                            text-white
                            px-8
                            py-3
                            rounded-lg
                            hover:bg-stone-700
                            transition
                        ">
                            前往應徵
                        </a>
                    </div>

                </div>
            </div>

        </div>
    </div>
</template>
