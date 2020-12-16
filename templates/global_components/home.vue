<template id="page-home">
	<div>
		[[ message ]]
	</div>
</template>

<script type="text/javascript">
	
	Vue.component('my-page-home',{
		template: '#page-home',
		props: {
		},
		delimiters: ['[[',']]'],
		//vuetify: new Vuetify({}),
		data(){
			return {
				message:'Página Inicial'
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