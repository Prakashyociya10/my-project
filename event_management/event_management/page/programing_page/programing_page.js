frappe.pages['programing-page'].on_page_load = function(wrapper) {
    const page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Item List Page',
        single_column: true
    });

    page.set_primary_action('New Item', () => {
        frappe.new_doc('Item');
    }, 'octicon octicon-plus');

    const $container = $(wrapper).find('.layout-main-section');
    $container.html('<h3>📦 All Items</h3><div id="item-table">Loading...</div>');

    // 🔄 Call backend Python method that uses frappe.get_all
    frappe.call({
        method: "event_management.event_management.page.programing_page.programing_page.get_all_items",  // Make sure this matches your whitelisted Python method path
        callback: function(res) {
            const items = res.message;
            console.log(items)

            if (!items || !items.length) {
                $('#item-table').html('<p>No items found.</p>');
                return;
            }

            let html = `
                <table class="table table-bordered">
                    <thead> 
                        <tr>
                            <th>Item Name</th>
                            <th>Item Group</th>
                            <th>Item Code</th>
                            <th>Status</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
            `;

            items.forEach(item => {
                const status = item.disabled ? 'Disabled' : 'Enabled';
            
                html += `
                    <tr>
                        <td>${item.name}</td>
                        <td>${item.item_group}</td>
                        <td>${item.item_code || '-'}</td>
                        <td>${status}</td>
                        <td><a class="btn btn-sm btn-primary" href="/app/item/${item.name}">View</a></td>
                    </tr>
                `;
            });
            
            html += `</tbody></table>`;
            $('#item-table').html(html);
        }
    });
};
