from flask import render_template


class PageMaker:
    def make_restautants_list_page(self, rests_query):
        return render_template('web/restaurants_list_page.html', rests_query=rests_query)

    def make_resgister_page(self, form):
        return render_template('web/register_restaurant.html', form=form)

    def make_update_page(self, form):
        return render_template('web/update_restaurant.html', form=form)


        
