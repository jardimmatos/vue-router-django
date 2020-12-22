<template id="page-login">
	<div>
		[[ message ]]
		
	</div>
</template>

<script type="text/javascript">
	
	Vue.component('my-page-login',{
		template: '#page-login',
		props: {
		},
		delimiters: ['[[',']]'],
		//vuetify: new Vuetify({}),
		data(){
			return {
				message:'Página Login'
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