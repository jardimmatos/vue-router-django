<template id="component-tooltip">
	<div>
		<template>
			<v-tooltip transition="fade" :color="color" outlined :top="position=='top'" :right="position=='right'" :left="position=='left'" :bottom="position=='bottom'">
				<template v-slot:activator="{ on }">
					<span v-on="on">
						<slot name="content"></slot>						
					</span>
				</template>
				<span :class="textColor">
					<slot name="message">
						[[computedMessage]]
					</slot>						
				</span>
			</v-tooltip>			
		</template>
	</div>
</template>

<script type="text/javascript">
	
	Vue.component('my-tooltip',{
		template: '#component-tooltip',
		props: {
			color:{
				type: String,
				default: 'black',
			},
			message:{
				type:String,
				default: '',
			},
			textColor:{
				type:String,
				default: 'white--text',
			},
			position:{
				type:String,
				default: 'top',
			}
		},
		delimiters: ['[[',']]'],
		//vuetify: new Vuetify({}),
		data(){
			return {
			}
		},
		methods:{
		},
		mounted(){
		},
		created(){
		},
		computed:{
			computedMessage(){
				return this.message
			}
		},
		watch:{
		}
	});
</script>