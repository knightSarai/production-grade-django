import { Component, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { RouterModule } from '@angular/router';


export const getCookie = (name: string):string => {
  const value = '; ' + document.cookie;
  const parts = value.split('; ' + name + '=');
  if (parts.length === 2) {
    return parts.pop()?.split(';').shift() ?? '';
  }
  return ''
}


@Component({
  standalone: true,
  imports: [RouterModule],
  selector: 'org-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
    title = 'trainees';
    http = inject(HttpClient);

    ngOnInit() {
        this.verifySession();
    }

    getRequest() {
        this.http.get('/api/test', {withCredentials: true}).subscribe(console.log);
    }

    postRequest() {
        this.http
            .post('/api/test',
                { test: 'test' },
                {
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken'),
                    },
                    withCredentials: true
                }
            )
            .subscribe(console.log);
    }

  verifySession() {
    this.http
      .get('/api/auth/verify-session', {withCredentials: true})
      .subscribe(console.log);
  }


}
