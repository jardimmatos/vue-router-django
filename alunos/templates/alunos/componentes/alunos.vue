<template id="page-alunos">
	<div>
		[[message]]
	</div>
</template>

<script type="text/javascript">
	
	Vue.component('my-page-alunos',{
		template: '#page-alunos',
		props: {
		},
		delimiters: ['[[',']]'],
		//vuetify: new Vuetify({}),
		data(){
			return {
				message:'Página Alunos'
			}
		},
		methods:{
		},
		mounted(){
		},
		created(){
		},
		computed:{
			
		},
		watch:{
		}
	});
</script>